//logged out

let home = document.querySelector('.home')
let about = document.querySelector('.about')
let contact = document.querySelector('.contact')
let login = document.querySelector('.login')
let about_select = document.querySelector('.selecta')
let home_select = document.querySelector('.selecth')
let contact_select = document.querySelector('.selectc')
let login_select = document.querySelector('.selectl')
var body = document.querySelector('.body')
var header = document.querySelector('.header')

var home_page = document.querySelector('.home_container')
var about_page = document.querySelector('.about_container')



window.addEventListener('load',()=>{
    home.classList.toggle('s')
    home_select.classList.toggle('ss')
    header.classList.toggle('invisible')
    body.classList.toggle('splash')
    setTimeout(() => {
        body.classList.toggle('splash')
        header.classList.toggle('invisible')
    }, 2500);
})


about.addEventListener('click',()=>{

    if (home.classList.contains('s')){
    
        home.classList.toggle('s')
        home_select.classList.toggle('ss')
    }

    if (contact.classList.contains('s')){
    
        contact.classList.toggle('s')
        contact_select.classList.toggle('ss')
    }

    if (login.classList.contains('s')){
    
        login.classList.toggle('s')
        login_select.classList.toggle('ss')
    }

    if (!about.classList.contains('s')){
        about.classList.toggle('s')
        about_select.classList.toggle('ss')
    }

})

home.addEventListener('click',()=>{
    if (!home.classList.contains('s')){
    
        home.classList.toggle('s')
        home_select.classList.toggle('ss')
    }

    if (contact.classList.contains('s')){
    
        contact.classList.toggle('s')
        contact_select.classList.toggle('ss')
    }

    if (login.classList.contains('s')){
    
        login.classList.toggle('s')
        login_select.classList.toggle('ss')
    }

    if (about.classList.contains('s')){
        about.classList.toggle('s')
        about_select.classList.toggle('ss')
    }


})

contact.addEventListener('click',()=>{
    if (home.classList.contains('s')){
    
        home.classList.toggle('s')
        home_select.classList.toggle('ss')
    }

    if (!contact.classList.contains('s')){
    
        contact.classList.toggle('s')
        contact_select.classList.toggle('ss')
    }

    if (login.classList.contains('s')){
    
        login.classList.toggle('s')
        login_select.classList.toggle('ss')
    }

    if (about.classList.contains('s')){
        about.classList.toggle('s')
        about_select.classList.toggle('ss')
    }
})

login.addEventListener('click',()=>{
    if (home.classList.contains('s')){
        home.classList.toggle('s')
        home_select.classList.toggle('ss')
    }

    if (contact.classList.contains('s')){
    
        contact.classList.toggle('s')
        contact_select.classList.toggle('ss')
    }

    if (!login.classList.contains('s')){
    
        login.classList.toggle('s')
        login_select.classList.toggle('ss')
    }

    if (about.classList.contains('s')){
        about.classList.toggle('s')
        about_select.classList.toggle('ss')
    }
})




function select(a,b){

    if(about.classList.contains('s')||contact.classList.contains('s')||login.classList.contains('s')||home.classList.contains('s')){
        active == true
        deactivate(a1,a2)
    }else{
        active == true
    }

    if(active){
        a1 == a
        a2 == b
        a.classList.toggle('s')
        b.classList.toggle('ss')
        active == false
    }

}

function deactivate(a,b){
    if (a.classList.contains('s')){
        a.classList.toggle('s')
        b.classList.toggle('ss')
    }
}


