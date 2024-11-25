
const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.slider-btn.prev');
const nextButton = document.querySelector('.slider-btn.next');
const slideWidth = slider.clientWidth;


function moveNext() {
    if (slider.scrollLeft + slideWidth >= slider.scrollWidth) {
        slider.scrollTo({ left: 0, behavior: 'smooth' }); // Regresar al inicio si estamos al final
    } else {
        slider.scrollBy({ left: slideWidth, behavior: 'smooth' });
    }
}

// Manejador para el botón de anterior
prevButton.addEventListener('click', () => {
    slider.scrollBy({ left: -slideWidth, behavior: 'smooth' });
    resetAutoSlide(); // Reinicia el temporizador
});

// Manejador para el botón de siguiente
nextButton.addEventListener('click', () => {
    moveNext();
    resetAutoSlide(); // Reinicia el temporizador
});

// Temporizador automático
let autoSlideInterval = setInterval(moveNext, 4000); // Cambia cada 3 segundos

// Función para reiniciar el temporizador
function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    autoSlideInterval = setInterval(moveNext, 3000);
}
