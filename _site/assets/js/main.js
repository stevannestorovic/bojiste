const navSlide = () => {
    console.log('nav slide');
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");

    burger.addEventListener('click', (e) => {
        nav.classList.toggle('nav-active');
    });
}
console.log("main loaded");
navSlide();
