const parent = document.getElementById("seccionPreguntas");
const secRef = document.getElementById("seccionAñadir");
const opcionElegida = document.getElementById("opcionAñadir");
const temp = document.getElementsByTagName("template");
for(i = 0; i < temp.length; i++)
{
    temp[i].content.querySelector("div");
}

document.getElementById("selAñadir").addEventListener("click", añadir);

function añadir()
{
    //var newDiv = document.createElement("div");
    //parent.insertBefore(newDiv, secRef)
    var newDiv = temp[0].content.firstElementChild.cloneNode(true);
    var divBody;
    if(opcionElegida.value == "Opción múltiple")
    {
        divBody = temp[1].content.firstElementChild.cloneNode(true);
    }
    else
    {
        divBody = temp[2].content.firstElementChild.cloneNode(true);
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
    console.log("hola");

    pregunta.remove();
}