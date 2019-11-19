var funcionario = {
	nome:"Joao",
	cargo:"Cozinheiro",
	cor:"Negra",
	sexo:"M",
	gravidez: false,
	displayFuncionario: function(){
		console.log(this.nome);
	}
	 
};


var displayFuncionariosButton = document.getElementById("displayFuncionariosButton");

displayFuncionariosButton.addEventListener('click', function(){
	funcionario.displayFuncionario();
});

var handlers = {
	displayFuncionarios: function(){
		funcionario.displayFuncionario()
	}
};



