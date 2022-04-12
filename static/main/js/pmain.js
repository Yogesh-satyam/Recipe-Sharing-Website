('.profilenav ul li').click(function()
{
    $(this).addclass("active").siblings().removeClass('active');
})
const tbtn = document.querySelectorAll('.profilenav ul li');


function tabs(panelIndex){
    const tab = document.querySelectorAll('.tab');
    tab.forEach(function(node){
        node.style.display='none';
    });
    tab[panelIndex].style.display='block';
}
tabs(0);