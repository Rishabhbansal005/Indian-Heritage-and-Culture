document.addEventListener('DOMContentLoaded', () => {
    
    const elementsToAnimate = document.querySelectorAll('.head, .images');

   
    const observerOptions = {
        root: null, 
        rootMargin: '0px', 
        threshold: 0.1 
    };

    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                
                entry.target.classList.add('is-in-view'); 
                observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);

   
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });

 

});