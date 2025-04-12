
window.revelar =  ScrollReveal({ reset: true });

revelar.reveal('.box_odd', 
    { 
        duration: 1500, 
        x: '50px',
        y : '50px' ,
        easing: 'ease-in-out',
    },
);

revelar.reveal('.box_even', 
    {
        duration: 1500, 
        x: '50px',
        y : '50px' ,
        easing: 'ease-in-out',
    }
);

revelar.reveal('.revel_delay', 
    {
        duration: 2000, 
        x: '60px',
        y : '50px' ,
        easing: 'ease-in-out',
    }
);


revelar.reveal('.contato_left', 
    {
        duration: 2000, 
        distance: '50px',
        origin: 'left',
        easing: 'ease-in-out',
    }
);

revelar.reveal('.contato_right', 
    {
        duration: 2000, 
        distance: '50px',
        origin: 'rigth',
        easing: 'ease-in-out',
    }
);


revelar.reveal('.contato_view1', {duration: 2500, distance: '80px',origin: 'top',easing: 'ease-in-out',});
revelar.reveal('.contato_view2', {duration: 3000, distance: '80px',origin: 'top',easing: 'ease-in-out',});
revelar.reveal('.contato_view3', {duration: 3500, distance: '80px',origin: 'top',easing: 'ease-in-out',});
revelar.reveal('.contato_view4', {duration: 4000, distance: '80px',origin: 'top',easing: 'ease-in-out',});
revelar.reveal('.contato_view5', {duration: 5000, distance: '80px',origin: 'top',easing: 'ease-in-out',});


