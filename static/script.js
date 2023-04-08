m = document.getElementsByClassName("modal")[0];
ob = document.getElementsByClassName("modal-open")[0];
cb = document.getElementsByClassName("modal-close")[0];
console.log(m)
ob.addEventListener("click", gg);
function gg() {
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