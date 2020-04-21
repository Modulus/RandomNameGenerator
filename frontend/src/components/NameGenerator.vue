<template>
  <div class="container">
    <div class="jumbotron jumbotron-fluid">
      <h1 class="header">Name Generator</h1>
      
      <p class="subText">
        Click the large "Generate" button, to generate names
      </p>

      <div class="clicketido">
        <b-button size="lg" class="" variant="success" v-on:click="generateName()">Generate&nbsp;<b-icon icon="arrow-repeat"></b-icon></b-button>
        <b-button size="lg" variant="danger" v-on:click="clear()">Clear&nbsp;<b-icon icon="trash"></b-icon></b-button>
      </div>

      <div class="results" v-if="data">
          <p class="mainText">
            {{ data.first | capitalize }} {{ data.second | capitalize}}
          </p>
            <p style="display: none;" class="badge badge-dark">{{data.first | makeId}}-{{data.second | makeId }}</p>
        </div>
  <div>
    test
        <b-button variant="primary" size="lg">Male<font-awesome-icon icon="mars" /></b-button>
        <b-button variant="danger" size="lg">Female<font-awesome-icon icon="venus" /></b-button>
<font-awesome-icon icon="user-secret" />
  </div>
        <div class="error" v-if="error">
          Something failed!!!
        </div>


      <!--- Card container -->
      <div class="row">
        <div class="col-sm-3">
          <b-card
            title="Animal"
            img-src="../assets/animals.png"
            img-alt="Animals"
            img-top
            tag="animals"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
            Generate animal names
            </b-card-text>
          <b-button class="buttons" variant="primary" size="lg"><font-awesome-icon icon="mars" /></b-button>
          <b-button class="buttons" variant="success" size="lg"><font-awesome-icon icon="venus" /></b-button>
          </b-card>
        </div>
        <div class="col-sm-3">
          
            <b-card
              title="Norwegian"
              img-src="../assets/animals.png"
              img-alt="Norwegian"
              img-top
              tag="norwegian"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
              Generate norwegian names
              </b-card-text>
            <b-button class="buttons" variant="primary" size="lg"><font-awesome-icon icon="mars" /></b-button>
            <b-button class="buttons" variant="success" size="lg"><font-awesome-icon icon="venus" /></b-button>
            </b-card>

        </div>
        <div class="col-sm-3">
                  <b-card
          title="Norse"
          img-src="../assets/norse.png"
          img-alt="Norse"
          img-top
          tag="norse"
          style="max-width: 20rem;"
          class="mb-2"
        >
          <b-card-text>
           Generate norse names
          </b-card-text>
        <b-button class="buttons" variant="primary" size="lg"><font-awesome-icon icon="mars" /></b-button>
        <b-button class="buttons" variant="success" size="lg"><font-awesome-icon icon="venus" /></b-button>
        </b-card>
        </div>
        <div class="col-sm-3">
                  <b-card
          title="Weird"
          img-src="../assets/funny.png"
          img-alt="Weird"
          img-top
          tag="weird"
          style="max-width: 20rem;"
          class="mb-2"
        >
          <b-card-text>
           Generate weird names
          </b-card-text>
        <b-button class="buttons" variant="primary" size="lg"><font-awesome-icon icon="mars" /></b-button>
        <b-button class="buttons" variant="success" size="lg"><font-awesome-icon icon="venus" /></b-button>
        </b-card>
        </div>
      </div>




    <!-- LARGE ICONS: https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons-->
    </div>

    <div class="inputs">
      <h3>Type</h3>
      TODO
      <hr/>

      <h3>Gender</h3>
      TODO
      <hr />
    </div>

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
      type: "norwegian",
      gender: "female",
      error: null
  }
},
methods : {
  generateName(){
    fetch("http://localhost:5000/?type=" + this.type+"&gender="+ this.gender)
      .then(stream => stream.json())
      .then(data => {
        this.data = {
          first: data.first,
          second: data.second,
          timestamp: data.timestamp
        }
        this.error = null
        console.log("Created new name at servetime: " + this.data.timestamp)
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
    this.error = null
  },

},
filters: {
  capitalize: function (value) {
    if (!value) return ""
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
  },
  makeId: function(value){
    if (!value) return ""
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

.buttons {
  margin-right: 2em;
}

.buttons b-icon {
  padding-left: 5em;
}

.buttons b-icon {
  padding-left: 5em;
}

b-button {
  padding-right: 5em;
}
</style>
