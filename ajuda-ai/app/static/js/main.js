document.addEventListener("DOMContentLoaded", function() {

    const botoes = document.querySelectorAll("button, .btn");

    botoes.forEach(function(botao) {
        botao.addEventListener("click", function() {
            botao.style.transform = "scale(0.97)";

            setTimeout(function() {
                botao.style.transform = "";
            }, 120);
        });
    });

    const mensagens = document.querySelectorAll(".erro, .sucesso");

    mensagens.forEach(function(mensagem) {
        setTimeout(function() {
            mensagem.style.opacity = "0";

            setTimeout(function() {
                mensagem.remove();
            }, 400);

        }, 5000);
    });

    const imagens = document.querySelectorAll("img");

    imagens.forEach(function(imagem) {
        imagem.addEventListener("error", function() {
            imagem.style.display = "none";
        });
    });

    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(function(link) {
        link.addEventListener("click", function(event) {
            const destino = document.querySelector(link.getAttribute("href"));

            if (destino) {
                event.preventDefault();

                destino.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    const formularios = document.querySelectorAll("form");

    formularios.forEach(function(formulario) {
        formulario.addEventListener("submit", function() {
            const botao = formulario.querySelector("button[type='submit']");

            if (botao) {
                botao.disabled = true;
                botao.style.opacity = "0.7";
                botao.textContent = "Enviando...";
            }
        });
    });

});