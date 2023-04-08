m = document.getElementsByClassName("modal")[0];
ob = document.getElementsByClassName("modal-open")[0];
cb = document.getElementsByClassName("modal-close")[0];
ob.addEventListener("click", gg);
function mfcc() {
    m.style.display = "block";
}

cb.onclick = function () {
    m.style.display = "none";
}
window.onclick = function (event) {
    console.log(event.target)
    if (event.target == m) {
        m.style.display = "none";
    }
}


m1= document.getElementsByClassName("modal")[1];
ob1 = document.getElementsByClassName("modal-open")[1];
cb1 = document.getElementsByClassName("modal-close")[1];
ob1.addEventListener("click", gg);
function gmm() {
    m1.style.display = "block";
}

cb1.onclick = function () {
    m1.style.display = "none";
}
window.onclick = function (event) {
    console.log(event.target)
    if (event.target == m) {
        m1.style.display = "none";
    }
}