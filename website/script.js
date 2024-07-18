const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureButton = document.getElementById('capture');
const results = document.getElementById('results');

navigator.mediaDevices.getUserMedia({video:true})
    .then(stream =>{
        video.srcOject = stream;
    });

captureButton.addEventListener('click',() =>{
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.clientWidth, canvas.height);
    const imageData = canvas.toDataURL('image/jpeg');

    fetch('/recommend', {
        method: 'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({image: imageData})
    })
    .then(response => response.json())
    .then(data => {
        results.innerHTML = '';
        data.forEach(product => {
            results.innerHTML += `<p>${product.name} by ${product.brand} - ${product.color_code}</p>`; 
        });

        //Integrate AR with Three.js and AR.js
        initAR(data);
    });
});    

function initAR(products) {
    const arContainer = document.getElementById('ar-container');
    arContainer.innerHTML = '';

    const scene = document.createElement('a-scene');
    scene.setAttribute('embedded','');
    scene.setAttribute('arjs','sourceType:webcam; debugUIEnabled: false;');

    const camera = document.createElement('a-camera');
    camera.setAttribute('gps-camera', 'gpsMinDistance: 5;');
    scene.appendChild(camera);

    products.forEach(product => {
        const box = document.createElement('a-box');
        box.setAttribute('position','0 0.5 0');
        box.setAttribute('material',`color: ${product.color_code}`);
        box.setAttribute('gps-entity', 'latitude:0; longitude:0')
        scene.appendChild(box);
    });

    arContainer.appendChild(scene);
}