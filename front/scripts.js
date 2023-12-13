/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/amostras';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.amostras.forEach(item => insertList(
        item.id,
        item.ph,
        item.hardness,
        item.solids,
        item.chloramines,
        item.sulfate,
        item.conductivity,
        item.organic_carbon,
        item.trihalomethanes,
        item.turbidity,
        item.potability
      ))
    })
    .catch((error) => {
      console.error('Erro:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList();

/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputPh, inputHardness, inputSolids,
  inputChloramines, inputSulfate, inputConductivity,
  inputOrganicCarbon, inputTrihalomethanes, inputTurbidity) => {

  const formData = new FormData();
  formData.append('ph', inputPh);
  formData.append('hardness', inputHardness);
  formData.append('solids', inputSolids);
  formData.append('chloramines', inputChloramines);
  formData.append('sulfate', inputSulfate);
  formData.append('conductivity', inputConductivity);
  formData.append('organic_carbon', inputOrganicCarbon);
  formData.append('trihalomethanes', inputTrihalomethanes);
  formData.append('turbidity', inputTurbidity);

  let url = 'http://127.0.0.1:5000/amostra';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      } else {
        return response.json().then((errorData) => {
          throw new Error(`${errorData.message}`);
        });
      }
    })
    .then((data) => {
      insertList(data.id, data.ph, data.hardness, data.solids, data.chloramines,
        data.sulfate, data.conductivity, data.organic_carbon, data.trihalomethanes,
        data.turbidity, data.potability);
      alert("Item adicionado!");
    })
    .catch((error) => {
      console.error(error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (id) => {
  console.log(id);
  let url = 'http://127.0.0.1:5000/amostra?id=' + id;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Erro:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o clique no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const phItem = div.getElementsByTagName('td')[0].innerHTML;
      if (confirm("Você tem certeza?")) {
        div.remove();
        deleteItem(phItem);
        alert("Removido!");
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputPh = document.getElementById("newPh").value;
  let inputHardness = document.getElementById("newHardness").value;
  let inputSolids = document.getElementById("newSolids").value;
  let inputChloramines = document.getElementById("newChloramines").value;
  let inputSulfate = document.getElementById("newSulfate").value;
  let inputConductivity = document.getElementById("newConductivity").value;
  let inputOrganicCarbon = document.getElementById("newOrganicCarbon").value;
  let inputTrihalomethanes = document.getElementById("newTrihalomethanes").value;
  let inputTurbidity = document.getElementById("newTurbidity").value;


  if (inputPh === '' || inputHardness === '' || inputSolids === '' || inputChloramines === ''
    || inputSulfate === '' || inputConductivity === '' || inputOrganicCarbon === '' ||
    inputTrihalomethanes === '' || inputTurbidity === '') {
    alert("Preencha todos os campos!");
  } else if (isNaN(inputHardness) || isNaN(inputSolids) || isNaN(inputChloramines) || isNaN(inputSulfate) || isNaN(inputConductivity) || isNaN(inputOrganicCarbon) || isNaN(inputTrihalomethanes) || isNaN(inputTurbidity)) {
    alert("Estes campos precisam ser números!");
  } else {
    postItem(inputPh, inputHardness, inputSolids, inputChloramines, inputSulfate, inputConductivity, inputOrganicCarbon, inputTrihalomethanes, inputTurbidity);
  }

}

/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (id, ph, hardness, solids, chloramines, sulfate, conductivity, organicCarbon, trihalomethanes, turbidity, potability) => {
  var item = [id, ph, hardness, solids, chloramines, sulfate, conductivity, organicCarbon, trihalomethanes, turbidity, potability];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  insertButton(row.insertCell(-1))

  document.getElementById("newPh").value = "";
  document.getElementById("newHardness").value = "";
  document.getElementById("newSolids").value = "";
  document.getElementById("newChloramines").value = "";
  document.getElementById("newSulfate").value = "";
  document.getElementById("newConductivity").value = "";
  document.getElementById("newOrganicCarbon").value = "";
  document.getElementById("newTrihalomethanes").value = "";
  document.getElementById("newTurbidity").value = "";

  removeElement();
}

/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let button = document.createElement("button");
  let txt = document.createTextNode("\u00D7");
  button.className = "btn btn-secundary close";
  button.appendChild(txt);
  parent.appendChild(button);
}