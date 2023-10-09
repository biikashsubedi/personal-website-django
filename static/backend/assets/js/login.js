const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const video = document.getElementById('video-element')
const image = document.getElementById('img-element')
const captureBtn = document.getElementById('capture-btn')
const pinInput = document.getElementById('pin');
const pinError = document.getElementById('errorMessage');

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: true})
        .then((stream) => {
            video.srcObject = stream
            const {height, width} = stream.getTracks()[0].getSettings()

            pinInput.addEventListener('focus', () => {
                pinInput.classList.remove('is-invalid');
                pinError.textContent = '';
            });

            captureBtn.addEventListener('click', e => {
                e.preventDefault()
                if (pinInput.value.trim() === '') {
                    pinInput.classList.add('is-invalid');
                    pinError.textContent = 'Pin is Required While Processing With Face Id.';
                    return
                }
                captureBtn.classList.add('not-visible')
                const track = stream.getVideoTracks()[0]
                const imageCapture = new ImageCapture(track)

                imageCapture.takePhoto().then(blob => {
                    const img = new Image(width, height)
                    img.src = URL.createObjectURL(blob)
                    image.append(img)

                    video.classList.add('not-visible')

                    const reader = new FileReader()

                    reader.readAsDataURL(blob)
                    reader.onloadend = () => {
                        const base64data = reader.result

                        const fd = new FormData()
                        fd.append('csrfmiddlewaretoken', csrftoken)
                        fd.append('photo', base64data)
                        fd.append('pin', pinInput.value)

                        $.ajax({
                            type: 'POST',
                            url: '/classify/',
                            enctype: 'multipart/form-data',
                            data: fd,
                            processData: false,
                            contentType: false,
                            success: (resp) => {
                                console.log(resp)
                                if (resp.success) {
                                    window.location.href = '/home'
                                }
                                window.location.href = '/face-login/'
                            },
                            error: (err) => {
                                console.log(err)
                            }
                        })
                    }
                }).catch(error => {
                    console.log('takePhoto() error: ', error);
                });
            });
        })
        .catch(error => {
            console.log("Something went wrong!", error);
        });
}
