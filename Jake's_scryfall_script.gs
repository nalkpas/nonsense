//TODO: fix color conditional formatting.
//Better header bar formatting.
//Organize cards by type.
//Different Land and Artifact sheets.
//Fix resetSheets

function resetSheets() {
 var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  spreadsheet.getSheets().forEach(function(sheet) {
    if (sheet.getName() != "untitled") {
      spreadsheet.deleteSheet(sheet);
    }
  });
}

function cardToRow(atts) {
  if (atts.type_line.search("Creature") != -1) {
    if (atts.card_faces) {
      creature = atts.card_faces[0];
      adventure = atts.card_faces[1];
      cmc = creature.cmc + " // " + adventure.cmc;
      oracle_text = creature.oracle_text + "\n----------------\n" + adventure.oracle_text;
      return [atts.name, atts.cmc, atts.type_line, oracle_text, atts.power, atts.toughness];
    }
    return [atts.name, atts.cmc, atts.type_line, atts.oracle_text, atts.power, atts.toughness];
  } else {
    return [atts.name, atts.cmc, atts.type_line, atts.oracle_text, " ", " "]; //Empty Strings for Conditional Formatting Rules.
  }
}

function sheetName(color, rarity) {
  Logger.log(color);
  switch(rarity) {
    case "common":
      return color + "(C)";
    case "uncommon":
      return color + "(U)";
  }
  return color + "(R)";
}

function arrayToColor(colors) {
  if(colors.length > 1) {
    return "M";
  }
  if(colors.length == 0) {
   return "A";
  }
  return colors[0];
}

function styleSheet() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  spreadsheet.getSheets().forEach(function(sheet) {
    header = sheet.getRange("A1:F1");
    header.setBorder(true, true, true, true, false, true);
    header.setFontWeight("Bold");
    header.setB
    color = sheet.getName()[0];
    Logger.log(sheet.getName());
    Logger.log(color);
    switch(color) {
      case "W":
        color_name='#fffbe0';
        break;
      case "U":
        color_name='#c7d3ff';
        break;
      case "B":
        color_name='#c4c6cf';
        break;
      case "R":
        color_name='#f2c4c4';
        break;
      case "G":
        color_name='#c4f2d2';
        break;
      case "M":
        color_name='#f4d99a';
        break;
      case "A":
        color_name='#dbdbdb';
        break;
    }
    sheet.setTabColor(color_name);
    var rule = SpreadsheetApp.newConditionalFormatRule()
    .whenCellNotEmpty()
    .setRanges([sheet.getRange("A1:F20")])
    .setBackground(color_name).build();
    sheet.setConditionalFormatRules([rule]);

    sheet.autoResizeColumns(1, 2);
    sheet.autoResizeColumns(5, 6);
    sheet.setColumnWidth(3, 200);
    sheet.setColumnWidth(4, 400);
  });
}
function populateCardData() {
  var url = "https://api.scryfall.com/cards/collection"
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var colors = ["W", "U", "B", "R", "G", "M", "A"];
  var rarities = ["common", "uncommon", "rares"];
  colors.forEach(function(color) {
    rarities.forEach(function(rarity) {
      name = sheetName(color, rarity)
      spreadsheet.insertSheet(name);
      spreadsheet.getSheetByName(name).appendRow(["name","cmc","type","text","pwr","tgh"]);
    });
  });

  sheet = spreadsheet.getActiveSheet();
  for (i=1; i<=249; i++) {
    var payload = {"identifiers":[{"set":"thb","collector_number":""+i}]}
    var options =
        {
          'method'  : 'POST',
          'contentType': 'application/json',
          'payload' : JSON.stringify(payload),
          'followRedirects' : true,
          'muteHttpExceptions': true
        };
    var result = UrlFetchApp.fetch(url, options);
    card = JSON.parse(result);
    atts = card.data[0];
    color = arrayToColor(atts.colors);
    rarity = atts.rarity;
    sheet = spreadsheet.getSheetByName(sheetName(color, rarity));
    row = cardToRow(atts);
    sheet.appendRow(row);
    Utilities.sleep(50);
  }
}
