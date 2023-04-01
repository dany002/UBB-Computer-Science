const backgroundButton = document.getElementById('backgroundButton');
const linkButton = document.getElementById('linkButton');
const links = document.querySelectorAll('a');
let bgIndex = 1;
let linkColor = 'green';

backgroundButton.addEventListener('click', () => {
    switch(bgIndex) {
        case 1:
            document.body.style.backgroundImage = "url('resources/mercury.jpg')";
            break;
        case 2:
            document.body.style.backgroundImage = "url('resources/venus.jpg')";
            break;
        case 3:
            document.body.style.backgroundImage = "url('resources/earth.jpg')";
            break;
        case 4:
            document.body.style.backgroundImage = "url('resources/mars.jpg')";
            break;
        case 5:
            document.body.style.backgroundImage = "url('resources/sun.jpg')";
            bgIndex = 0;
            break;
    }
    bgIndex++;
});

linkButton.addEventListener('click', () => {
    if(linkColor === 'green') {
        links.forEach(link => link.style.color = 'purple');
        linkColor = 'purple';
    } else {
        links.forEach(link => link.style.color = 'green');
        linkColor = 'green';
    }
});