function onOpen() {
  var yybkcat = SpreadsheetApp.getActiveSpreadsheet();
  var menu = [
    {name: "Edit Book", functionName: 'editBook'} 
  ];
  yybkcat.addMenu("YY Catalog", menu);
  
}

function editBook() {
  var yybkcat = SpreadsheetApp.getActiveSpreadsheet();
  var booklist = yybkcat.getActiveSheet();
  if(booklist.getName()!="booklist") {
    Browser.msgBox("switch to booklist");
    return;
  }
  
  if(booklist.getActiveCell().getRow()==1) {
    booklist.insertRowAfter(1);
    booklist.getRange(2,1).activate();
  }
  
  /* gather field name and values */
  var names = colnames(booklist);
  var values = booklist.getRange(booklist.getActiveCell().getRow(), 1, 
                               1, names.length).getValues()[0];
  
  var app = UiApp.createApplication().setWidth(400).setHeight(600);
  var panel = app.createVerticalPanel();
  var grid = app.createGrid(names.length, 2);

  for(var ifield = 0; ifield != names.length; ++ifield) {
    grid.setWidget(ifield, 0, app.createLabel(names[ifield]).setStyleAttribute('text-align', 'right'));
    grid.setWidget(ifield, 1,
                   app.createTextBox()
                   .setWidth(300)
                   .setName(names[ifield])
                   .setValue(values[ifield])
                   .addValueChangeHandler(app.createServerHandler('field_changed')));
  }
  
  panel.add(grid);
  panel.add(app.createButton("OK")
            .setStyleAttribute("margin-top", "40")
            .setStyleAttribute("margin-left", "150")
            .addClickHandler(app.createServerClickHandler('closeApp')));
  
  app.add(panel);
  yybkcat.show(app);
}
      
function field_changed (e) {
  var booklist = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  /* gather field name and values */
  for(var icol = 1; icol!=20; ++icol) {
    var name = booklist.getRange(1, icol).getValue()
        .toString().trim();
    if(e.parameter.hasOwnProperty(name)) {
      booklist.getRange(booklist.getActiveCell().getRow(), icol)
        .setValue(e.parameter[name]);
      break;
    }
  }
}

function closeApp() {
  return UiApp.getActiveApplication().close();
}


/** data processing */
function colnames(sheet) {
  var names = [];  
  for(var icol=1;; ++icol) {
    var name = sheet.getRange(1, icol).getValue()
        .toString().trim();
    if(!name)
      break;
    names.push(name);
  }
  
  
  return names;
}
