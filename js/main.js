//Swiper
var swiper = new Swiper(".popular-content", {
    
    slidesPerView: 4,
    spaceBetween:4,
    
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    pagination:{
        el: ".swiper-pagination",
        clickable:true,
    },
    navigation:{
        nextE1: ".swiper-button-next",
        prevE1: ".swiper-button-prev",
    },
    breakpoints: {
        280: {
            slidePerView: 1,
            spaceBetween: 10,
        },
        320: {
            slidePerView: 2,
            spaceBetween: 10,
        },
        540: {
            slidePerView: 3,
            spaceBetween: 15,
        },
        900: {
            slidePerView: 4,
            spaceBetween: 20,
        },
    },
});