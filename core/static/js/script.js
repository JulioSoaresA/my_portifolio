document.addEventListener("DOMContentLoaded", function () {
    const myObservert = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            } else {
                entry.target.classList.remove("show");
            }
        });
    });

    const elements = document.querySelectorAll(".hidden");

    elements.forEach((element) => myObservert.observe(element));
});

document.addEventListener("DOMContentLoaded", function () {
    let menuIcon = document.querySelector("#menu-icon");
    let navbar = document.querySelector(".navbar");

    menuIcon.onclick = () => {
        menuIcon.classList.toggle("bx-x");
        navbar.classList.toggle("active");
    };
});

document.addEventListener("DOMContentLoaded", function () {
    var fullText = document.getElementById("about-text").innerHTML;
    var truncatedText = fullText.substring(0, 200) + "...";
    var isTruncated = true;
    var btn = document.getElementById("read-more-btn");
    var paragraph = document.getElementById("about-text");

    // Initially show truncated text
    paragraph.innerHTML = truncatedText;

    btn.addEventListener("click", function (event) {
        event.preventDefault();
        if (isTruncated) {
            paragraph.innerHTML = fullText;
            btn.textContent = "Leia Menos";
        } else {
            paragraph.innerHTML = truncatedText;
            btn.textContent = "Leia Mais";
        }
        isTruncated = !isTruncated;
    });
});

document.getElementById("download-btn").addEventListener("click", function () {
    var cvId = this.getAttribute("data-cv-id");
    fetch(`/download-cv/${cvId}/`)
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                window.location.href = data.download_url;
            } else {
                alert("Erro ao baixar o CV.");
            }
        })
        .catch((error) => console.error("Erro:", error));
});