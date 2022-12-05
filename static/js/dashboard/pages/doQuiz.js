const principal = document.getElementById("principal");
const seccionTitulo = document.getElementById("seccionTitulo")
const seccionPreguntas = document.getElementById("seccionPreguntas")
const tamañoVent = document.querySelector('.auth-content');
const formStart = document.getElementsByTagName("form")[0];

var alias;
var csrf;

document.getElementById("iniciarQuiz").addEventListener("click", initQuiz);

function initQuiz()
{
    if(formStart.reportValidity())
    {
        alias = principal.firstElementChild.getElementsByTagName("input")[1].value;
        csrf = $('input[name=csrfmiddlewaretoken').val();
        principal.firstElementChild.remove();
        
        tamañoVent.style.width = '800px';
        seccionTitulo.removeAttribute('hidden');
        seccionPreguntas.removeAttribute('hidden');

        var btnEnviar = document.getElementById("enviar");
        btnEnviar.addEventListener("click", enviarQuiz);
    }
}

function añadir()
{
    //var newDiv = document.createElement("div");
    //parent.insertBefore(newDiv, secRef)
    var newDiv = temp[0].content.firstElementChild.cloneNode(true);
    var divBody;
    if(opcionElegida.value == "Opción múltiple")
    {
        divBody = temp[1].content.firstElementChild.cloneNode(true);
        newDiv.firstElementChild.classList.add("elegir");
    }
    else
    {
        divBody = temp[2].content.firstElementChild.cloneNode(true);
        newDiv.firstElementChild.classList.add("llenar");
    }

    newDiv.children[0].appendChild(divBody);

    var btnQuitar = newDiv.children[0].getElementsByClassName("btn-danger")[0];
    btnQuitar.addEventListener("click", () => {
        eliminarPregunta(newDiv);
    });

    parent.insertBefore(newDiv, secRef);
}

function eliminarPregunta(pregunta)
{
    pregunta.remove();
}

function enviarQuiz()
{
    let nPreguntas = Array.from(seccionPreguntas.children).filter(el => el.tagName === 'DIV');
    var respuestas = [];
    for(i = 0; i < nPreguntas.length; i++)
    {
        var opciones = nPreguntas[i].getElementsByTagName('input');
        if(nPreguntas[i].classList[1] == 'elegir')
        {
            respuestas[i] = [];
            for(j = 0; j < opciones.length; j++)
            {
                respuestas[i][j] = opciones[j].checked;
            }
        }
        else
        {
            respuestas[i] = opciones[0].value;
        }
    }
    //console.log(respuestas);
    //console.log(alias);

    let cookie = document.cookie
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

    let datos = {
        quiz : new URL(location.href).pathname,
        alias : alias,
        respuestas : JSON.stringify(respuestas),
        csrfmiddlewaretoken : csrfToken
    }

    $.ajax({
        type: "POST",
        url: "send-quiz",
        data: datos, //+ "&csrfmiddlewaretoken=" + $('input[name=csrfmiddlewaretoken').val(),
        //data: JSON.stringify(sendInfo),
        success:function(text){
            //alert('Successfull');
            if (text == "success") {
                console.log("Success");
                msgEnviado();
            } else {
                console.log("Error");
            }
        }
    });
}

function msgEnviado()
{
    seccionPreguntas.remove();
    principal.getElementsByTagName('h3')[0].innerHTML = 'Su respuesta se ha enviado';
}