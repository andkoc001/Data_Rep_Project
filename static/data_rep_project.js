/*
Data Representation Project, GMIT 2020
Author: Andrzej Kocielski, G00376291@gmit.ie
GitHub: 
Lecturer: Dr. Andrew Beatty
*/
// ////////////////////


// ////////////////////
// Table CRUD manipulation

function showTable() {
  document.getElementById('showCreateButton').style.display = "inline"
  document.getElementById('equipmentTable').style.display = "table"
  document.getElementById('createUpdateForm').style.display = "none"
  document.getElementById('createLabel').style.display = "inline"
  document.getElementById('updateLabel').style.display = "none"
  document.getElementById('doCreateButton').style.display = "none"
  document.getElementById('doUpdateButton').style.display = "none"
  document.getElementById('showExportButton').style.display = "block"
}

function showCreate() {
  document.getElementById('showCreateButton').style.display = "none"
  document.getElementById('equipmentTable').style.display = "none"
  document.getElementById('createUpdateForm').style.display = "block"
  document.getElementById('createLabel').style.display = "inline"
  document.getElementById('updateLabel').style.display = "none"
  document.getElementById('doCreateButton').style.display = "block"
  document.getElementById('doUpdateButton').style.display = "none"
  document.getElementById('showExportButton').style.display = "none"
}


function showViewAll() {
  document.getElementById('showCreateButton').style.display = "block"
  document.getElementById('equipmentTable').style.display = "table"
  document.getElementById('createUpdateForm').style.display = "none"
}


function showUpdate(buttonElement) {
  document.getElementById('showCreateButton').style.display = "none"
  document.getElementById('equipmentTable').style.display = "none"
  document.getElementById('createUpdateForm').style.display = "block"
  document.getElementById('createLabel').style.display = "none"
  document.getElementById('updateLabel').style.display = "inline"
  document.getElementById('doCreateButton').style.display = "none"
  document.getElementById('doUpdateButton').style.display = "block"
  document.getElementById('showExportButton').style.display = "none"

  var rowElement = buttonElement.parentNode.parentNode
  // these is a way of finding the closest <tr> which would safer, closest()
  var equipment = getEquipmentFromRow(rowElement)
  populateFormWithEquipment(equipment)
}


function doCreate() {
  var form = document.getElementById('createUpdateForm')
  var equipment = {}
  console.log("inside doCreate function:")
  console.log(JSON.stringify(equipment)) // for testing
  equipment.category = form.querySelector('select[placeholder="Category"]').value
  equipment.name = form.querySelector('input[placeholder="Name"]').value
  equipment.supplier = form.querySelector('input[placeholder="Supplier"]').value
  equipment.price_eur = form.querySelector('input[placeholder="Price EUR"]').value
  console.log(JSON.stringify(equipment)) // for testing
  createEquipmentAjax(equipment)
  showViewAll()
}


function doUpdate() {
  console.log("inside doUpdate function");
  var equipment = getEquipmentFromForm();
  var rowElement = document.getElementById(equipment.id);
  console.log("inside doUpdate function - will do updateEquipmentAjax in the next line");
  console.log(JSON.stringify(equipment));
  updateEquipmentAjax(equipment);
  setEquipmentInRow(rowElement, equipment);
  clearForm();
  showViewAll();
}


function doDelete(r) {
  var tableElement = document.getElementById('equipmentTable');
  var rowElement = r.parentNode.parentNode;
  var index = rowElement.rowIndex;
  deleteEquipmentAjax(rowElement.getAttribute("id"));
  tableElement.deleteRow(index);
}

function doExport() {
  var equipmentList = document.getElementById('equipmentTable');
  exportAjax()
}


function addEquipmentToTable(equipment) {
  var tableElement = document.getElementById('equipmentTable')
  var rowElement = tableElement.insertRow(-1)
  rowElement.setAttribute('id', equipment.id)
  var cell1 = rowElement.insertCell(0);
  cell1.innerHTML = equipment.id
  var cell2 = rowElement.insertCell(1);
  cell2.innerHTML = equipment.category
  var cell3 = rowElement.insertCell(2);
  cell3.innerHTML = equipment.name
  var cell4 = rowElement.insertCell(3);
  cell4.innerHTML = equipment.supplier
  var cell5 = rowElement.insertCell(4);
  cell5.innerHTML = parseFloat(equipment.price_eur).toFixed(2)
  /*
  var cell6 = rowElement.insertCell(5); //
  cell6.innerHTML = '<button class="checkBitcoin" onclick="checkBitcoin(this)">Check</button>'
  */
  var cell6 = rowElement.insertCell(5);
  cell6.innerHTML = '<button class="table_entry_update" onclick="showUpdate(this)">Update</button>'
  var cell7 = rowElement.insertCell(6);
  cell7.innerHTML = '<button class="table_entry_delete" onclick="doDelete(this)">Delete</button>'
}


function clearForm() {
  var form = document.getElementById('createUpdateForm')
  form.querySelector('select[placeholder="Category"]').value = ''
  form.querySelector('input[placeholder="Name"]').value = ''
  form.querySelector('input[placeholder="Supplier"]').value = ''
  form.querySelector('input[placeholder="Price EUR"]').value = ''
}


function getEquipmentFromRow(rowElement) {
  var equipment = {}
  equipment.id = rowElement.getAttribute('id')
  equipment.category = rowElement.cells[1].firstChild.textContent
  equipment.name = rowElement.cells[2].firstChild.textContent
  equipment.supplier = rowElement.cells[3].firstChild.textContent
  equipment.price_eur = parseFloat(rowElement.cells[4].firstChild.textContent, 2)
  console.log(equipment)
  return equipment
}


function setEquipmentInRow(rowElement, equipment) {
  rowElement.cells[0].firstChild.textContent = equipment.id
  rowElement.cells[1].firstChild.textContent = equipment.category
  rowElement.cells[2].firstChild.textContent = equipment.name
  rowElement.cells[3].firstChild.textContent = equipment.supplier
  rowElement.cells[4].firstChild.textContent = parseFloat(equipment.price_eur).toFixed(2)
}


function populateFormWithEquipment(equipment) {
  var form = document.getElementById('createUpdateForm')
  console.log(form)
  form.querySelector('input[name="id"]').disabled = true
  form.querySelector('input[name="id"]').value = equipment.id
  form.querySelector('select[placeholder="Category"]').value = equipment.category
  form.querySelector('input[placeholder="Name"]').value = equipment.name
  form.querySelector('input[placeholder="Supplier"]').value = equipment.supplier
  form.querySelector('input[placeholder="Price EUR"]').value = equipment.price_eur
  return equipment
}


function getEquipmentFromForm() {
  var form = document.getElementById('createUpdateForm')
  var equipment = {}
  // console.log("AAAAAA, id:")
  equipment.id = form.querySelector('input[name="id"]').value
  // console.log(equipment.id)
  // console.log("AAAAAA, category:")
  equipment.category = form.querySelector('select[placeholder="Category"]').value
  // console.log(equipment.category)
  // console.log("AAAAAA, name:")
  equipment.name = form.querySelector('input[placeholder="Name"]').value
  // console.log(equipment.name)
  // console.log("AAAAAA, supplier:")
  equipment.supplier = form.querySelector('input[placeholder="Supplier"]').value
  // console.log(equipment.supplier)
  // console.log("AAAAAA, price:")
  equipment.price_eur = parseFloat(form.querySelector('input[placeholder="Price EUR"]').value).toFixed(2)
  // console.log(equipment.price_eur)
  // console.log("inside getEquipmentFromForm, next line prints equipment")
  // console.log(JSON.stringify(equipment))
  // console.log("still inside getEquipmentFromForm")
  return equipment
}

// ////////////////////
// AJAX 

host = window.location.origin

function exportAjax() {
  $.ajax({
    "url": host + "/equipment",
    "method": "GET",
    "data": "",
    "dataType": "JSON",
    "success": function (result) {
      // console.log(result);
      for (equipment of result) {
        console.log(equipment);
      }
    },
    "error": function (xhr, status, error) {
      console.log("error: " + status + " msg:" + error);
    }
  });
}



function getAllAjax() {
  $.ajax({
    "url": host + "/equipment",
    "method": "GET",
    "data": "",
    "dataType": "JSON",
    "success": function (result) {
      //console.log(result);
      for (equipment of result) {
        addEquipmentToTable(equipment);
      }
    },
    "error": function (xhr, status, error) {
      console.log("error: " + status + " msg:" + error);
    }
  });
}


function createEquipmentAjax(equipment) {
  console.log("inside createEquipmentAjax function:")
  console.log(JSON.stringify(equipment)); // for testing
  $.ajax({
    "url": host + "/equipment",
    "method": "POST",
    "data": JSON.stringify(equipment),
    "dataType": "JSON",
    contentType: "application/json; charset=utf-8",
    "success": function (result) {
      console.log(result);
      equipment.id = result.id
      addEquipmentToTable(equipment)
      clearForm()
      showViewAll()
    },
    "error": function (xhr, status, error) {
      console.log("error: " + status + " msg:" + error);
    }
  });
}


function updateEquipmentAjax(equipment) {
  console.log("inside updateEqimpmentAjax function");
  console.log(JSON.stringify(equipment));
  $.ajax({
    "url": host + "/equipment/" + encodeURI(equipment.id),
    "method": "PUT",
    "data": JSON.stringify(equipment),
    //"data": buildQuery(equipment),
    "dataType": "JSON",
    contentType: "application/json; charset=utf-8",
    "success": function (result) {
      console.log(result);
    },
    "error": function (xhr, status, error) {
      console.log("error: " + status + " msg: " + error);
    }
  });
}


function deleteEquipmentAjax(id) {

  //console.log(JSON.stringify('deleting '+id));
  $.ajax({
    "url": host + "/equipment/" + encodeURI(id),
    "method": "DELETE",
    "data": "",
    "dataType": "JSON",
    contentType: "application/json; charset=utf-8",
    "success": function (result) {
      //console.log(result);

    },
    "error": function (xhr, status, error) {
      console.log("error: " + status + " msg:" + error);
    }
  });
}
getAllAjax();


function readJSON() {
  $.ajax({
    "url": "https://api.coindesk.com/v1/bpi/currentprice.json ",
    "method": "GET",
    "data": "",
    "dataType": "JSON",
    "success": function (result) {
      //console.log(result);
      var rate = result.bpi.EUR.rate
      document.getElementById("outputBitcoin").innerText = rate;
    },
    "error": function (xhr, status, error) {
      //console.log("error: " + status + " msg:" + error);
      var rate = result.bpi.EUR.rate
      document.getElementById("outputBitcoin").innerText = rate;
    }
  });
}

// from https://stackoverflow.com/a/16017283
function buildQuery(obj) {
  var Result = '';
  if (typeof (obj) == 'object') {
    jQuery.each(obj, function (key, value) {
      Result += (Result) ? '&' : '';
      if (typeof (value) == 'object' && value.length) {
        for (var i = 0; i < value.length; i++) {
          Result += [key + '[]', encodeURIComponent(value[i])].join('=');
        }
      } else {
        Result += [key, encodeURIComponent(value)].join('=');
      }
    });
  }
  console.log("inside buildQuery")
  return Result;
}

// ////////////////////
// Scroll up to top of page functionality
// Adopted from: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

// Get signal from the button
var mybutton = document.getElementById("toTop");

// The button appears when the user scrolls down 50px from the top of the document
window.onscroll = function () { scrollFunction() };
function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// ////////////////////
// Input validation

// -----------------
// Login to server

// Adopted from: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form_modal
// Open the modal (login box)
var modal = document.getElementById('login_pop');

// -----------------
// The following is a JavaScript verification function 
// Adopted from: https://www.daniweb.com/programming/web-development/code/330933/a-simple-html-login-page-using-javascript
// Disabled (not in use) because of its limits; the built-in HTML5 form verification is used instead
function check(form) {
  // the following code checkes whether the entered password is matching 
  if (form.u_name.value == "User" && form.psw.value == "GMIT") {
    window.open("start.html") // opens the target page while password matches
  }
}
