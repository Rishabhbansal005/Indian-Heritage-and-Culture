const toggle = document.querySelector('.toggle');
const dropdownMenu = document.querySelector('.dropdownmenu');

toggle.addEventListener('click', () => {
    dropdownMenu.classList.toggle('active');
});


