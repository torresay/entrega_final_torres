// Dropdown related for Type, Category and Subcategory 
$("#id_transaction").change(function () {
    var url = $("#TransactionForm").attr("dropdown-category-url");  
    var transactionID = $(this).val(); 

    $.ajax({                      
      url: url,                   
      data: {
        'transaction': transactionID    
      },
      success: function (data) {  
        console.log(data);
        $("#id_categoryTransaction").html(data);
        $("#id_subCategoryTransaction").html('<option value="">---------</option>');  
      }
    });

  });

$("#id_categoryTransaction").change(function () {
    var url = $("#TransactionForm").attr("dropdown-subcategory-url");  
    var categoryTransactionID = $(this).val(); 

    $.ajax({                      
      url: url,                   
      data: {
        'categoryTransaction': categoryTransactionID    
      },
      success: function (data) {  
        $("#id_subCategoryTransaction").html(data);  
      }
    });

  });

// SAVE TRANSACTIONAL WALLET FOR LATER
const getFormData = () => {

  const formId = "TransactionForm"; // ID of the form

  let form = document.querySelector(`#${formId}`); // select form

  let formElements = form.elements; // get the elements in the form

  let date = new Date();

  let draft_name = prompt('Enter the name of the Draft here:');

  let data = { }; // create an empty object with the formIdentifier as the key and an empty object as its value

  console.log(data)

  for (const element of formElements) {
    if (element.name.length > 0) {
      data[element.name] = element.value;      
    }
  }

  data['date'] = date;

  data['name'] = draft_name;

  return data;
};

const saveButton = document.querySelector("#save"); // select save button
saveButton.onclick = event => {

  event.preventDefault(); 
  
  data = getFormData();
  
  var drafts = localStorage.getItem('drafts');
  

  if (drafts == null || Object.keys(JSON.parse(drafts)).length === 0 ) {
    drafts = {}
    id = 1
    console.log("True")
  }
  else{
    drafts = JSON.parse(drafts)
    id = Object.keys(drafts)[Object.keys(drafts).length - 1]
    console.log(id)
    id = parseInt(id)+1
    console.log("False")
  }
  
  drafts[id]= data;
  
  localStorage.setItem('drafts', JSON.stringify(drafts));
  
  console.log("Formulario creado")
};