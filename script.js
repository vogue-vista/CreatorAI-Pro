async function creerVideo(){


const theme = document.getElementById("theme").value;

const plateforme = document.getElementById("plateforme").value;

const style = document.getElementById("style").value;

const ton = document.getElementById("ton").value;

const duree = document.getElementById("duree").value;



const resultat = document.getElementById("resultat");



if(theme === ""){

resultat.innerHTML = `
<p>⚠️ Écris un sujet avant de générer.</p>
`;

return;

}



resultat.innerHTML = `

<div class="attente">

⏳ CreatorAI prépare ta vidéo...

<br>

Analyse du sujet...

<br>

Création du script...

<br>

Optimisation du hook...

</div>

`;



try{


const response = await fetch("/api/generer",{


method:"POST",


headers:{


"Content-Type":"application/json"


},



body:JSON.stringify({


theme:theme,

plateforme:plateforme,

style:style,

ton:ton,

duree:duree


})


});




const data = await response.json();



if(data.erreur){


throw new Error(data.erreur);


}




resultat.innerHTML = `


<div class="resultatIA">


<h3>🎬 Résultat CreatorAI</h3>


<pre>

${data.resultat}

</pre>


</div>


`;




}



catch(error){



resultat.innerHTML = `


<h3>❌ Erreur</h3>

<p>

Impossible de contacter l'intelligence artificielle.

</p>


<small>

${error.message}

</small>


`;



console.log(error);



}


}
