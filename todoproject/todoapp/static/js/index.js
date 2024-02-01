let h = document.getElementById('x')
let f = document.getElementById('form')
let b = document.getElementById('bk')

function add(){
    console.log("clicked")
    if(f.style.display === "none"){
        f.style.display = "flex"
        h.style.display = "none"

    }else{
        f.style.display = "flex"
        h.style.display = "none"
    }
}

function bk(){
    console.log("clicked")
    f.style.display = "none"
    h.style.display = "flex"
}