# Client Builder Tutorial
## Tutorial Overview
This tutorial guides a developer through lessons in the using the Client Builder feature of the [VANTIQ IDE](../../..). Clients are browser-based web applications with (a) the ability to display data stored in the VANTIQ system in a variety of forms (graphs, gauges, tables) and (b) accept data from the user of the client either to be displayed and/or stored in the VANTIQ system. The Client Builder allows the developer to write small amounts of Javascript which implements the logic behind the client, such as responses to button pushes and data entry.

The tutorial lessons show the developer how to create a simple invoicing client application. This client displays a form to create and submit a simple invoice, displays a table which dynamically updates the last five submitted invoices, and displays a gauge which dynamically displays the sum of the last five submitted invoices.

All lessons assume the developer has a working knowledge of the [VANTIQ IDE](../../..). It is recommended that a new developer completes the lessons in the [Introductory Tutorial](tutorial/index.html) before starting the lessons in this tutorial.

Note: if needed, you can import a finished version of this project using the _Projects -> Import_ menu item.  Just select _Tutorials_ for Import Type, then select _Client Builder_ from the second drop-down, then click _Import_.

## 1: Creating a Client Builder Project
The first task is to create a project in the IDE to assemble all the client components.

Use the **Projects** button, select **New Project**, which displays the New Project Wizard. Either create a new Namespace (recommended) or add a new project to the current Namespace, select **Empty** as the Project type, and title the project "Invoice":

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ClientProject](../assets/img/client/EMProject.png "Create Client Project")

The rest of the lessons take place inside this Project.

## 2: Creating a Data Type
The invoice client needs to store invoice data input by the user in the VANTIQ system. You must create a data type to specify that data.

Use the **Add** button to select **Type...**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![AddType](../assets/img/client/TutAddType.png "Add Invoice Type")

Use the **New Type** button to create the invoice data type:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![CreateInvoice](../assets/img/client/TutCreateInvoice1.PNG "Create Invoice Type")

Use the resulting popup to name your type "Invoice". The description is optional, but you must leave the role as standard. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![CreateInvoice](../assets/img/client/TutCreateInvoice2.PNG "Create Invoice Type")

The _Invoice_ type contains six properties:

```text
* amount: a Real property which is the total amount of the invoice
* description: an (optional) String property which describes what is being invoiced
* firstName: an (optional) String property which holds the first name of the purchaser
* ID: a unique String property which is used to reference the invoice
* lastName: a String property which holds the last name of the purchaser
* timestamp: a DateTime property which holds the date and time that the invoice is submitted
```

The invoice client creates the _ID_ and _timestamp_ properties using Javascript. The user of the invoice client will manually enter all other properties.

Once the six properties are defined, use the **Save** button to save the _Invoice_ type. Use the **Save** button in the top left corner of the IDE to save the project.

## 3: Creating the Invoice Client
This lesson uses the IDE's Client Builder feature to create our invoice client.

Use the **Add** button to select **Client...**, then use the **New Client** button to display the New Client dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![NewCB](../assets/img/intro/NewClient.png "New Client")

Enter "Invoice" as the Client Name and use the default **Design for browser** radio button since we'll be running our client in a browser. Use the **OK** button to display the Client Builder:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![NewCB](../assets/img/intro/NewCB.png "New Client Builder") 

The rest of this tutorial takes place inside this Client Builder.
    
## 4: Creating the Client Invoice Form
The next task is to create the invoice data entry form. This is multi-step process and demonstrates concepts of the Client Builder common to many clients.

First, we'll need to create a new Data Object for the client. Data Objects define Javascript variables that are referenced by the client. In this invoice client, we need to define one Data Object which is used to hold the invoice properties (firstName, lastName, etc.) the user enters. To create a new Data Object, use the **Data Objects** button to display the drop down menu, then select _page.data for page 'Start'_ to open the _Editing Data Object_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![DataObjects](../assets/img/client/TutDataObjects.png "Create Data Object")

Use the **Choose Type** pull-down menu to select _Invoice_, then use the **Add a 'Typed Object' based on Type:** button to add the new _Invoice_ property to the list of Data Objects. By creating the _Invoice_ property, any Javascript may now reference the _Invoice_ variable using the following syntax: _page.data.Invoice_. (_page.data_ is the client's syntax prefix to reference the data object associated with the client.)

Second, we'll use the Client Builder to automatically create a data entry form based on the _Invoice_ properties. Use the **Generate Widgets** icon, which is found under the  heading and looks like a small lightning bolt. The Generate Widgets process creates two data entry widgets for each property of the _Invoice_ type (a text widget which is the name of the property and an edit widget which allows for the actual data entry) plus a container widget to hold the data entry widgets.

Use the **Save and Exit** button to save the new _Invoice_ Data Object.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceForm](../assets/img/client/TutInvoiceForm.png "Create Invoice Form")

Third, we'll edit the data entry form to make it a little more user friendly. Since we'll use Javascript to automatically generate the invoice _ID_ and _timestamp_ properties, delete those widgets from the client display. Select the _timestamp_ title widget by tapping on it then use the **Delete** button just above the palette of widgets to delete the title. In the same manner, select and delete the _timestamp_ data entry widget, the _ID_ title widget, and the _ID_ data entry widget. 

Next, change the titles of the remaining widgets. To change the title of the _amount_ widget, tap on that title, then edit the _Text_ property to contain "Amount". In the same manner, change the titles of the _description_, _firstName_, and _lastName_ title widgets to "Description", "First Name" and "Last Name". Finally, drag and drop the _Last Name_ title widget and its data entry widget so they are directly under the _First Name_ widgets. The data entry form should now look like this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceFormEdit](../assets/img/client/TutInvoiceFormEdit.png "Create Invoice Form Edited")

Fourth, add a button to the form to submit the invoice data. To add the **Submit** button, drag the **Inline** widget palette tile (under _Buttons_) and drop it just under the _Last Name_ title in the form. By default, the button is titled 'Click Me'. Tap the 'Click Me' button to display its property sheet:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![SubmitButton](../assets/img/client/TutSubmitButton.png "Create Submit Button")

Change the _Button Label_ field in **Specific** property category to "Submit". Next, select the **Event** property category then tap the **<None\>** field titled _On Click_ to display the 'Edit Javascript' dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![SubmitJavascript](../assets/img/client/TutSubmitJavascript.png "Submit Javascript")

This dialog is where we enter Javascript that is executed whenever the user taps the **Submit** button. For our invoice client, we want to generate values for the _ID_ and _timestamp_ properties, validate some user-provided invoice properties, and submit the invoice data to the VANTIQ system:

```js
	// generateUUID is used to create a unique ID to use as the invoice ID
	generateUUID = function() {
        // http://www.ietf.org/rfc/rfc4122.txt
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 36; i++)
        {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
        s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
        s[8] = s[13] = s[18] = s[23] = "-";

        var uuid = s.join("");
        return uuid;
    };

	if (!page.data.Invoice.lastName || (page.data.Invoice.amount === 0)) {
        client.errorDialog("Please enter Last Name and Amount values!");
    } else {
        // programatically generate a timestamp and ID for our invoice
        page.data.Invoice.timestamp = new Date().toISOString();
        page.data.Invoice.ID = generateUUID();

        // create a VANTIQ database connection to insert our new invoice
        var http = new Http();
        http.setVantiqUrlForResource("Invoice");
        http.setVantiqHeaders();
        http.insert(page.data.Invoice, null, function(response) {
            client.infoDialog("Invoice " + page.data.Invoice.ID + " submitted.");            
        }, function(errors) {
            client.errorDialog("Submit fails: " + JSON.stringify(errors));
        });
    }
```

Use the **OK** button to save the Javascript and return to the property sheet.

Fifth, add a button to the form to reset the invoice data. To add the **Reset Form** button, drag the **Inline** widget palette tile and drop it to the right of the **Submit** button. Tap the new 'Click Me' button to display its property sheet:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![SubmitButton](../assets/img/client/TutSubmitButton.png "Create Submit Button")

Change the _Button Label_ field to "Reset Form". Next, select the **Event** property category then tap the **<None\>** field titled _On Click_ to display the 'Edit Javascript' dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![SubmitJavascript](../assets/img/client/TutResetJavascript.png "Submit Javascript")

This dialog is where we enter Javascript that is executed whenever the user taps the **Reset Form** button. For our invoice client, we want to reset the data entry form fields:

```js
	page.data.Invoice.firstName = page.data.Invoice.lastName = page.data.Invoice.description = "";
	page.data.Invoice.amount = null;
```

Use the **OK** button to save the Javascript and return to the property sheet.

The data entry form should now look like this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceFormEdit](../assets/img/client/TutInvoiceFormEdit2.png "Create Invoice Form Edited")

## 5: Creating a Recent Invoices Table
The next task is to create a table that displays the last five entered invoices. This is a two step process: (1) creating a Data Stream which is used to retrieve invoice data and (2) creating a table to display the data.

First, create a Data Stream. Use the **Data Stream** button to display the 'Edit Data Stream' dialog, then use the **New Data Stream** button to create the new Data Stream:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceDataModel](../assets/img/client/TutInvoiceDataModel.png "Create Invoice Data Stream")

Select the **On Timed Query** option then title the Data Stream "Invoice Queryable". A Timed Query Data Stream means that the client will retrieve data from the VANTIQ database on a periodic basis. Select _Invoice_ as the 'Data Type' since we want to retrieve invoice data. Enter 15 as the 'Update Interval' to retrieve the invoice data every 15 seconds. Since the goal is to create a table that displays the last five entered invoices, enable the **Limit maximum number of records to return** and enter '5'. Then select _timestamp_ as the 'Sort By' property (since we want to sort by when the invoice was created) and, finally, enable **Sort Descending** so the top entry in the table will be the most recent invoice. Use the **Save** button to save the Data Stream.

Second, create a table to hold the recent invoice data. To add the table, drag the **Table** widget palette tile (under _Data Display_) and drop it to the right of the data entry form. Tap the new table to display its property sheet:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Table](../assets/img/client/TutTable.png "Create Table")

Select the **Data** property category then use the **Data Stream** pull-down menu to select _Invoice Queryable_, our recently created Data Stream. Use the **Columns** property to display the 'Edit Columns' dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ConfigureTable](../assets/img/client/TutEditColumns.png "Configure Table")

Use the right arrows to add all six properties of the _Invoice_ type as table columns, then use the **OK** button to save the column configuration.

Finally, turn on **Clear on Data Arrival** so the table only displays the latest result from the Timed Query. Turn off **Show Paging** to clean up the display.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ConfigureTable](../assets/img/client/TutTableProp.png "Configure Table Display")
 
## 6: Creating a Recent Invoices Gauge
The next task is to create a gauge that displays the sum of the last five entered invoices. This is a four step process: (1) creating a new Data Object to hold the sum, (2) creating a new Data Stream that uses the Data Object, (3) creating the gauge to display the data and (4) adding Javascript to compute the sum.

First, create a Data Object. To create a new Data Object, use the **Data Objects** button to display the dropdown menu, then select _client.data_ to show the the '_Editing Data Object_' dialog. We select _client.data_ because our upcoming Data Stream may only reference _client.data_ Data Objects.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceDOSum](../assets/img/client/TutDOSum.png "Create Invoice Data Object")

 Use the **Add a Property** button to add the new Data Object: enter _sumLastFive_ as the Property Name, select _Typed Object_ from the **DataType** pull-down menu, and enter _sumLastFive_ as the Default Label. (Please refer to the [Client Builder User's Guide](../cbuser/index.html#models) for more information about Typed Objects.) The _sumLastFive_ Data Object is now present but we need to add one field to hold the actual invoice sum. Use the **Edit Typed Object** icon, which is found under the **--Actions--** menu heading and looks like a small pencil:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceDOSumProperty](../assets/img/client/TutDOSumProperty.png "Create Invoice Data Object Property")

Use the **Add a Property** button to add the new Typed Object property: enter _value_ as the Property Name, select _Real_ from the **DataType** pull-down menu, and enter _value_ as the Default Label. The _value_ property of the _sumLastFive_ Data Object will be used to hold the sum of the recent invoices. Use the **OK** button to save the _value_ property, then use the **Save and Exit** button to save the _sumLastFive_ Data Object.

Second, create a Data Stream which is used to send data events to the gauge. To create a new Data Stream, use the **Data Streams** button to display the '_Edit Data Streams_' dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![InvoiceDSSum](../assets/img/client/TutDSSum.png "Create Invoice Data Stream")

Click '_New Data Stream_', then select the **On Client Event** option then title the Data Stream “Invoice Sum”. Select **Get schema from client.data.object** then select _client.data.sumLastFive_ from the **Data Object** pull-down menu. This data stream now references the _sumLastFive_ Data Object we created in the previous step. Use the **Save** button to save the Data Stream.

Third, create a gauge to display the invoice sum. To add the gauge, drag the **Gauge** widget palette tile (under _Data Display_) and drop it under the invoice table. Tap the new gauge to display its property sheet:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Gauge](../assets/img/client/TutGauge.png "Create Gauge")

Select the **Data** property category then use the **Data Stream** pull-down menu to select _Invoice Sum_, our recently created Data Stream. Use the **Data Stream Property** pull-down men to select _value_. Since we're anticipating high-value invoices, select the **Specific** property category then enter the following property values:
```text
 Medium Range Zones: 700
 High Range Zones 900
 Maximum: 1000
```
Fourth, we will modify our submit Javascript to sum the recent invoices, then send the Client Event to update the Data Stream. Tap the **Submit** button in the data entry form. Next, tap the **Click to Edit** field titled _On Click_ to display the 'Edit Javascript' dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![SubmitJavascript](../assets/img/client/TutSubmitJavascript.png "Submit Javascript")

Here is the modified Javascript which includes summing the recent invoice values and sending the client event to the _Invoice Sum_ Data Stream:

```js
	// generateUUID is used to create a unique ID to use as the invoice ID
    generateUUID = function() {
        // http://www.ietf.org/rfc/rfc4122.txt
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 36; i++)
        {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
        s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
        s[8] = s[13] = s[18] = s[23] = "-";

        var uuid = s.join("");
        return uuid;
    };

    if (!page.data.Invoice.lastName || (page.data.Invoice.amount === 0)) {
        client.errorDialog("Please enter Last Name and Amount values!");
    } else {
        // programatically generate a timestamp and ID for our invoice
        page.data.Invoice.timestamp = new Date().toISOString();
        page.data.Invoice.ID = generateUUID();

        // create a VANTIQ database connection to insert our new invoice
        var http = new Http();
        http.setVantiqUrlForResource("Invoice");
        http.setVantiqHeaders();
        http.insert(page.data.Invoice.values, null, function(response) {
            // the invoice was saved, now query for the last five invoices based on timestamp
            client.infoDialog("Invoice " + page.data.Invoice.ID + " submitted.");
            var parameters = {
                "limit":5,
                "sort":{"timestamp":-1}
            };
            http.select(parameters, function(response) {
                // sum the amounts of the last five invoices
                client.data.sumLastFive.value = 0;
                for (var i = 0; i < response.length; i++) {
                    client.data.sumLastFive.value += response[i].amount;
                }
                // create a client event for widgets listening on the Invoice Sum data stream
                client.sendClientEvent("Invoice Sum", client.data.sumLastFive);
            }, function(errors) {
                client.errorDialog("Select fails: " + JSON.stringify(errors));
            });
        }, function(errors) {
            client.errorDialog("Submit fails: " + JSON.stringify(errors));
        });
    }
```

Use the **Save** button after adding the modifications to save the Javascript and return to the property sheet.

Our simple invoice client is complete and should look like this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![FinalClient](../assets/img/client/TutRunClient.png "Final Client")

Use the **Save** button to save the client and return to the Project. The _Project Resources Graph_ will look similar to this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![PRG](../assets/img/client/PRG.png "Project Resource Graph")

## 7: Running the Client
The last lesson of this tutorial is to run the client, entering sample invoices and watching the invoice table update. Click the _Client: Invoice_ oval in the _Project Resource Graph_ to display the Client Builder, then use the **Run** icon button of the _Client: Invoice_ pane (small triangle in a square at the top, right of the pane):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![RunClient](../assets/img/client/TutRunClient.png "Run Client")

To create a new invoice, add values to the _Amount_, _Description_, _First Name_, and _Last Name_ fields, then use the **Submit** button to submit the invoice. After entering several invoices, the client display will look similar to this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![RunClient](../assets/img/client/TutRunClient2.png "Run Client")

Use the **Stop Running** icon button of the _Client: Invoice_ pane (small square in a square at the top, right of the pane) to end the client session.
