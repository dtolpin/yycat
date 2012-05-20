function onOpen() {
  var yybkcat = SpreadsheetApp.getActiveSpreadsheet();
  var menu = [
    {name: "Edit Book", functionName: 'editBook'} 
  ];
  yybkcat.addMenu("YY Catalog", menu);
  
}

/** edit the book in the active row */
function editBook() {
  var yybkcat = SpreadsheetApp.getActiveSpreadsheet();
  var booklist = yybkcat.getActiveSheet();
  
  /* books are edited in the book list */
  if(booklist.getName()!="booklist") {
    Browser.msgBox("switch to booklist");
    return;
  }
  
  /* the first row is the column names, insert
   * an empty row after the first row and edit there */
  if(booklist.getActiveCell().getRow()==1) {
    booklist.insertRowAfter(1);
    booklist.getRange(2,1).activate();
  }
  
  var names = colnames_(booklist);
  var values = rowvalues_(booklist, names); /* in the active row */

  var app = UiApp.createApplication().setWidth(360).setHeight(480);
  var panel = app.createVerticalPanel();
  var buttons = app.createHorizontalPanel();
  
  panel.add(create_grid_(app, names, values));
  panel.add(buttons
            .add(
              app.createButton("Autofill")
              .addClickHandler(app.createServerClickHandler('autofill_')))
            .add(
              app.createButton("Suggest CN")
              .addClickHandler(app.createServerClickHandler('suggest_cn_')))
            .add(
              app.createButton("Close")
              .setStyleAttribute("margin-left", "150")
              .addClickHandler(app.createServerClickHandler('closeApp_'))));
            
       
  app.add(panel);
  yybkcat.show(app);
}
      
/** create grid holding field labels and entry boxes */
function create_grid_ (app, names, values) {
  var grid = app.createGrid(names.length, 2);

  for(var ifield = 0; ifield!=names.length; ++ifield) {
    if(names[ifield].charAt(0)=='_')
      continue; /* skip hidden fields */
    grid.setWidget(ifield, 0, app.createLabel(names[ifield])
                   .setStyleAttribute('text-align', 'right'));
    grid.setWidget(ifield, 1,
                   app.createTextBox()
                   .setWidth(280)
                   .setName(names[ifield])
                   .setValue(values[ifield])
                   .addValueChangeHandler(app.createServerHandler('field_changed_')));
  }
  
  return grid;
}

/** callback to store the changed field value */
/* it would nice to use closures for callbacks, but the API
 * does not allow this. The callback functions seem to be re-parsed/re-loaded/
 * called out of context, so the only way is to recompute the active row
 * and cell positions. */
function field_changed_ (e) {
  var booklist = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var names = colnames_(booklist);

  /* gather field name and values */
  var currow = booklist.getActiveCell().getRow();
  for(var icol = 1;icol!=names.length+1; ++icol) {
    var name = names[icol-1];
    if(e.parameter.hasOwnProperty(name)) {
      booklist.getRange(currow, icol)
        .setValue(e.parameter[name]);
      break;
    }
  }
}

function autofill_() {
  var booklist = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var names = colnames_(booklist);

  var currow = booklist.getActiveCell().getRow();
  var likerow = currow==2?3:currow-1;
  for(var icol = 1; icol!=names.length+1; ++icol) {
    var name = names[icol-1];
    if(["author", "title", "country", "city",  "publisher", "year"].indexOf(name)==-1)
      continue;
    if(booklist.getRange(currow, icol).isBlank())
      booklist.getRange(currow, icol).setValue(
        booklist.getRange(likerow, icol).getValue());
  }
  
  closeApp_();
  return editBook();
}

function suggest_cn_() {
  var booklist = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var names = colnames_(booklist);
  var values = rowvalues_(booklist, names);
  var record = {}, colno = {};
  
  for(var icol=1;icol!=names.length+1;++icol) {
    record[names[icol-1]] = values[icol-1];
    colno[names[icol-1]] = icol;
  }

      /* row and column indices */
  var currow = booklist.getActiveCell().getRow();
  var cncol = colno['call_number'],
      calcol = colno['_calc'],
      
      /* cells */
      cncell = booklist.getRange(currow, cncol),
      calcell = booklist.getRange(currow, calcol),
      
      /* symbolic range for call_number */
      cncolid = String.fromCharCode(cncol-1+'A'.charCodeAt(0));
      cns = cncolid+'2:'+cncolid+booklist.getLastRow();

  var call_number_prefix = 'אלג'
      + '\\' +record['author'].substring(0,3)
      + '\\' +record['title'].substring(0, 1);
  cncell.clear();
  for(var i=1;;++i) {
    var call_number = call_number_prefix+i;
    calcell.setFormula(
      "=QUERY("+cns+", \"SELECT A WHERE A='"+call_number+"'\")");
    if(calcell.getValue()!==call_number) {
      cncell.setValue(call_number);
      break;
    }
  }
  calcell.clear();
  
  closeApp_();
  return editBook();
}

function closeApp_() {
  return UiApp.getActiveApplication().close();
}


/** data processing */

/** retrieve the column names of a sheet */
function colnames_(sheet) {
  var names = [];  
  for(var icol=1; icol!=sheet.getLastColumn()+1; ++icol) {
    var name = sheet.getRange(1, icol).getValue()
        .toString().trim();
    if(name.length==0)
      break;
    names.push(name);
  }
  
  return names;
}

/** retrieve the row values in the active row */
function rowvalues_(sheet, names) {
  return sheet.getRange(sheet.getActiveCell().getRow(), 1, 
                        1, names.length).getValues()[0];
}
