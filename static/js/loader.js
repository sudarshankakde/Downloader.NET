var width = document.getElementsByTagName('body');
width = screen.width;



var height = document.getElementsByTagName('body');
height = screen.height;

var screensize= width+'x'+height;

localStorage.setItem('width', width);
localStorage.setItem('height', height);
localStorage.setItem('screensize',width+'x'+height);


window.addEventListener('load', loaded);
function loaded() {
        document.getElementById('loader').style.display = 'none';
        document.getElementById('ScreenSize').value = screensize
}



