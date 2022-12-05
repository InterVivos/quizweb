const parent = document.getElementById("seccionPreguntas");
const secRef = document.getElementById("seccionAñadir");
const opcionElegida = document.getElementById("opcionAñadir");
const temp = document.getElementsByTagName("template");
for(i = 0; i < temp.length; i++)
{
    temp[i].content.querySelector("div");
}

document.getElementById("selAñadir").addEventListener("click", añadir);
document.getElementById("btnGuardar").addEventListener("click", guardarQuiz);

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

function guardarQuiz()
{
    // initiate variables with form content
    //var email = $("#lemail").val();
    //var password = $("#lpassword").val();
    var titulo = document.getElementsByClassName("form-control-lg")[0].value;
    var contenido = [];
    let nPreguntas = parent.getElementsByClassName("card-header");
    for(i = 0; i < nPreguntas.length; i++)
    {
        contenido[i] = {};
        contenido[i].enunciado = nPreguntas[i].firstElementChild.firstElementChild.value;
        contenido[i].tipo = nPreguntas[i].classList[1];
        if(contenido[i].tipo == "elegir")
        {
            contenido[i].opciones = [];
            contenido[i].respuestas = [];
            let nOpciones = nPreguntas[i].lastElementChild.getElementsByTagName("input");
            for(j = 0; j < nOpciones.length/2; j++)
            {
                contenido[i].respuestas[j] =nOpciones[j*2].checked;
                contenido[i].opciones[j] =nOpciones[j*2+1].value;
            }
            //console.log(nOpciones);
        }
        else
        {
            contenido[i].respuesta = nPreguntas[i].lastElementChild.getElementsByTagName("input")[0].value;
        }
    }
    //console.log(contenido);

    //var url1 = new URL(location.href);
    //var nextPage = url1.searchParams.get("next");

    var sendInfo = {
        titulo: titulo,
        contenido: contenido
    }

    $.ajax({
        type: "POST",
        url: "save-quiz",
        //contentType: "application/json",
        //dataType: "json",
        data: "titulo=" + titulo + "&contenido=" + JSON.stringify(contenido), //+ "&csrfmiddlewaretoken=" + $('input[name=csrfmiddlewaretoken').val(),
        //data: JSON.stringify(sendInfo),
        success:function(text){
            //alert('Successfull');
            if (text == "success") {
                console.log("YAY");
            } else {
                console.log("oh no");
            }
        }
    });
}