<template>
  <div class="container">
    <h1 class="header">Name Generator</h1>
    
    <p class="subText">
      Click blue or green buttons in categories to generate names. To clear output area click the trash button.
    </p>
      <!--- Card container -->
      <div class="row">
        <div class="col-sm-3">
          <b-card
            header="Animal"
            footer="301 344 combinations"
            title=""
            img-alt="Animals"
            img-top
            tag="animals"
            style="max-width: 20rem;"
            class="mb-2">
              <b-img alt="Vue logo" src="animals.png" rounded></b-img>
            <!-- <b-card-text>
            Generate animal names
            </b-card-text> -->
          <b-button class="buttons" variant="primary" size="lg" v-on:click="generateName('animal', 'allgender')"><font-awesome-icon icon="paw"  /></b-button>
          </b-card>
        </div>
        <div class="col-sm-3">
          
            <b-card
              title=""
              img-alt="Norwegian"
              img-top
              tag="norwegian"
              style="max-width: 20rem;"
              class="mb-2"
              header="Norwegian"
              footer="2 716 000 combinations"
            >
            <b-img alt="Vue logo" src="norway.png" gluid-grow rounded></b-img>
              <!-- <b-card-text>
              Generate norwegian names
              </b-card-text> -->
            <b-button variant="primary" size="lg" v-on:click="generateName('norwegian', 'male')"><font-awesome-icon icon="mars" /></b-button> <b-button variant="success" size="lg" v-on:click="generateName('norwegian', 'female')"><font-awesome-icon icon="venus" /></b-button>
            </b-card>

        </div>


        <!-- img-src="../assets/norse.png" -->
        <div class="col-sm-3">
                  <b-card
          title=""
          img-alt="Norse"
          img-top
          tag="norse"
          style="max-width: 20rem;"
          class="mb-2"
          header="Norse"
          footer="166 796 combinations"          
        >
        <b-img alt="Vue logo" src="norse.png" rounded fluid-grow></b-img>
          <!-- <b-card-text>
           Generate norse names
          </b-card-text> -->
        <b-button class="buttons" variant="primary" size="lg" v-on:click="generateName('norse', 'male')"><font-awesome-icon icon="mars" /></b-button> <b-button class="buttons" variant="success" size="lg" v-on:click="generateName('norse', 'female')"><font-awesome-icon icon="venus" /></b-button>
        </b-card>
        </div>
          <!-- img-src="../assets/funny.png" -->

        <div class="col-sm-3">
                  <b-card
          title=""
          img-alt="Weird"
          img-top
          tag="weird"
          style="max-width: 20rem;"
          class="mb-2"
          header="Weirdness"
          footer="Hmmm combinations"          
        >
          <b-img alt="Vue logo" src="funny.png" rounded></b-img>
          <!-- <b-card-text>
           Generate weird names
          </b-card-text> -->
        <b-button class="buttons" variant="primary" size="lg" v-on:click="generateName('nynorsk', 'male')"><font-awesome-icon icon="mars" /></b-button> <b-button class="buttons" variant="success" size="lg" v-on:click="generateName('nynorsk', 'fenmale')"><font-awesome-icon icon="venus" /></b-button>
        </b-card>
        </div>
      </div>
      <b-row>
        <b-col></b-col>
        <b-col></b-col>
        <b-col><b-button block size="lg" variant="danger" v-on:click="clear()"><font-awesome-icon icon="trash" /></b-button></b-col> 
        <b-col></b-col>        
        <b-col></b-col>
      </b-row>

      <div class="results" v-if="data">
          <p class="mainText">
            {{ data.first | capitalize }} {{ data.second | capitalize}}
          </p>
            <p v-if="data.first" class="badge badge-dark">{{ makeId(data.first, data.second) }}</p>
        </div>

        <div class="error" v-if="error">
          Something failed!!!
        </div>

      <div v-if="data">
        <label for="tags-basic">Names this far</label>
        <b-form-tags input-id="newName" v-model="names" class="mb-2"></b-form-tags>
      </div>

    <!-- LARGE ICONS: https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons-->
    </div>

</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      data: {
        first: " ",
        second: " "
      },
      names: [],
      type: "norwegian",
      gender: "female",
      error: null
  }
},
methods : {
  generateName(type, gender){
    console.log("Fetching:" +process.env.VUE_APP_SERVICE_URL + "?type=" +type + "&gender=" + gender)

    fetch(process.env.VUE_APP_SERVICE_URL+"?type=" + type+"&gender="+ gender)
      .then(stream => stream.json())
      .then(data => {
        this.data = {
          first: data.first,
          second: data.second,
          timestamp: data.timestamp
        }
        this.error = null
        console.log("Created new name at servetime: " + this.data.timestamp)
        let name = this.capitalize(data.first).concat(" ").concat(this.capitalize(data.second))
        console.log("Pushing " + name + "to tag list")
        this.names.push(name)
      })
      .catch(error => {
        console.error(error)
        this.error = error
      })
  },
  clear(){
    this.data = {
      first: " ",
      second: " "
    }
    this.names = []
    this.error = null
  },
  makeId(first, second){
    console.log("First: "+ first +", second: " + second)
    if (!first || !second || first ===" " || second === " " || first.length == 0 || second.length == 0) return ""
    let value = first.concat(" ").concat(second)
    return value.split(" ").join("-")
  },
  capitalize: function (value) {
    if (!value) return ""
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
  },

},
filters: {
  capitalize: function (value) {
    if (!value) return ""
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
  },
  makeId: function(value){
    console.log("value is ["+value+"]")
    if (!value || value === "" || value.length == 0) return ""
    value = value.toString()
    return value.split(" ").join("-")
  }
}
// mounted(){
//     fetch("http://localhost:5000/")
//     .then(stream => stream.json()).then(data => this.data = data).catch(error => console.error(error))
//   }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

/* .buttons {
  margin: 2em;
}



.buttons font-awesome-icon {
  padding-left: 5em;
}

b-button {
  padding-right: 5em;
} */
</style>
