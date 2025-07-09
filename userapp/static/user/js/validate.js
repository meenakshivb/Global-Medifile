function OnlyNumbers(eleval,elename)
{
	if (isNaN(eleval)) {
		alert("Not a valid "+ elename +" number")
		return 0
	}
	return 1
}

function StringValidation(val, elename) {
	if (/^[a-zA-Z ]*$/.test(val))
	{
		return 1;
	}
alert ("Not a valid "+elename);
return 0;
}

function NoSpecialChars(val, elename) {
	if (/^[a-zA-Z0-9 ]*$/.test(val))
	{
		return 1;
	}
alert ("Special characters not allowed in "+ elename + " name");
return 0;
}

function RequiredFields(eleval,elename)
{
	if (eleval =="")
	{
		alert(elename+" field cannot be empty")
		return 0
	}
	return 1
}
function EmailValidation(em){
	if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(em))
		{
		return 1
		}
		alert("Not a valid E-mail Address")
		return 0	
}

function WebsiteValidation(em){
	if (/^\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(em))
		{
		return 1
		}
		alert("Not a valid Website Address")
		return 0	
}

function validate(){
	FName = document.getElementById('txtFName').value
	LName = document.getElementById('txtLName').value
	Company = document.getElementById('txtCompany').value
	Website = document.getElementById('txtWebsite').value
	Address = document.getElementById('txtAddress').value
	Phone = document.getElementById('txtPhone').value
	Email = document.getElementById('txtEmail').value
	Comments = document.getElementById('txtComments').value
	
/*	
	if (RequiredFields(FName,"First Name") == 0){
		document.getElementById('txtFName').focus()
		document.getElementById('txtFName').value = FName
		return false;
	}
	
	if (StringValidation(FName, "First Name") == 0){
		document.getElementById('txtFName').focus()
		document.getElementById('txtFName').value = FName
		return false;
	}
	
	if (StringValidation(LName, "Last Name") == 0){
		document.getElementById('txtLName').focus()
		document.getElementById('txtLName').value = LName
		return false;
	}
	
	if (NoSpecialChars(Company, "Company Name") == 0){
		document.getElementById('txtCompany').focus()
		document.getElementById('txtCompany').value = Company
		return false;
	}
	
	if(! Website == "")
	{
	if (WebsiteValidation(Website) == 0) {
		document.getElementById('txtWebsite').focus()
		document.getElementById('txtWebsite').value = Website
		return false;
	} 
	}
	
	if (RequiredFields(Email,"Email") == 0)	{
		document.getElementById('txtEmail').focus()
		document.getElementById('txtEmail').value = Email
		return false;
	}
	if (EmailValidation(Email) == 0) {
		document.getElementById('txtEmail').focus()
		document.getElementById('txtEmail').value = Email
		return false;
	} 
	
	if (RequiredFields(Phone,"Phone") == 0) {
		document.getElementById('txtPhone').focus()
		document.getElementById('txtPhone').value = Phone
		return false;
	}
	if (OnlyNumbers(Phone,"Phone") == 0) {
		document.getElementById('txtPhone').focus()
		document.getElementById('txtPhone').value = Phone
		return false;
	}
	
	if (RequiredFields(Address,"Address") == 0){
		document.getElementById('txtAddress').focus()
		document.getElementById('txtAddress').value = Address
		return false;
	}
*/	
			document.getElementById('h1').value = "1"
			return true;
}
