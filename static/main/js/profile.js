const p_div =document.querySelector('.profile-image');
const img= document.querySelector('#profile-photo');
const file=document.querySelectorAll('#file');
const upbtn=document.querySelector('#uplbutton');
img.addEventListener('mouseenter',function()
{
    upbtn.style.display='block';

});
img.addEventListener('mouseleave',function()
{
    upbtn.style.display='none';

});
file.addEventListener('change',function()
{
    const choosepic= this.file[0];
    if(choosepic)
    {
        const r= new FileReader();
        r.addEventListener('load',function()
        {
            img.setAttribute('src',r.result);
        });
        r.readAsDataURL(choosepic);
    }

});
