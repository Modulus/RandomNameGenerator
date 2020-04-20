<template>
  <div class="container">
    <div class="jumbotron jumbotron-fluid">
      <h1 class="header">Name Generator</h1>
      
      <p class="subText">
        Click the large "Generate" button, to generate names
      </p>
      <div class="clicketido">
        <b-button class="buttons" variant="success" v-on:click="generateName()">Generate&nbsp;<b-icon icon="arrow-repeat"></b-icon></b-button>
        <b-button variant="danger" v-on:click="clear()">Clear&nbsp;<b-icon icon="trash"></b-icon></b-button>
      </div>

      <div class="results" v-if="data">
          <p class="mainText">
            {{ data.first | capitalize }} {{ data.second | capitalize}}
          </p>
            <p style="display: none;" class="badge badge-dark">{{data.first | makeId}}-{{data.second | makeId }}</p>
        </div>

        <div class="error" v-if="error">
          Something failed!!!
        </div>


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
</style>
