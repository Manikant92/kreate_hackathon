<template>
  <div class="hello">
    <h2>Details</h2>
    <div class="details" v-if="person">
      <table id="person-table">
        <tr>
          <td>ID</td>
          <td>{{ person.id }}</td>
        </tr>
        <tr>
          <td>DOB</td>
          <td>{{ person.dob }}</td>
        </tr>
        <tr>
          <td>Name</td>
          <td>{{ person.name }}</td>
        </tr>
        <tr>
          <td>Name Match</td>
          <td :class="person.nameMatch | getColor">{{ person.nameMatch + '%'}}</td>
        </tr>
        <tr>
          <td>DOB Match</td>
          <td :class="person.dobMatch | getColor">{{ person.dobMatch + '%'}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SinglePerson',
  props: {
    id: String,
    person: null
  },
  created() {
    this.fetchDetails();
  },
  methods: {
    fetchDetails() {
      this.person = {
              id: 123723,
              name: 'Renuka Poluru',
              dob: '13/08/1994',
              nameMatch: 80,
              dobMatch: 100
          };
    }
  },
  filters: {
      getColor(percentage) {
          if(percentage == undefined || null) {
              return 'red'
          } else if(percentage >= 70) {
              return 'green'
          } else if(percentage >= 50) {
              return 'yellow'
          } else {
              return 'red'
          }
      },
  },
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
</style>
