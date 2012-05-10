function onOpen() {
  var yybkcat = SpreadsheetApp.getActiveSpreadsheet();
  var menu = [
    {name: "Edit Book", functionName: 'editBook'} 
  ];
  yybkcat.addMenu("YY Catalog", menu);
  
}

function editBook() {
  var yybkcat = SpreadsheetApp.getActiveSpreadsheet();
  if(yybkcat.getActiveSheet().getName()!="booklist") {
    showError(yybkcat, "switch to booklist");
    return;
  }
  var app = UiApp.createApplication();
  var button = app.createButton("OK");
  /* gather field name from the first row */
  /* gather field values from the current row */
  /* compute default values for empty fields */
  /* add entry fields to the form */
  app.add(button);
  yybkcat.show(app);
}

function showError(doc, msg) {
  var app = UiApp.createApplication().setHeight(60).setWidth(180);
  app.add(app.createHTML(
    "<span style=\"font-size: larger; font-weight: bold; color: #c00\">"
    +msg
    +"</span>"));
  app.add(app.createButton("OK").addClickHandler(app.createServerClickHandler('closeApp')));
  doc.show(app);
  return app;
}

function closeApp() {
  return UiApp.getActiveApplication().close();
}
