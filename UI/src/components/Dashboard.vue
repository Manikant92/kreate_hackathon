<template>
    <div id="dashboard">
        <Statistics v-if="statsCreated" :stats="stats" />
        <div id="dashboard-inner">
            <h2>Dashboard</h2>
            <input v-model="searchString" placeholder="Enter name" type="text"/>
            <select v-model="noOfRecords" placeholder="No. of Records">
                <option value="5">5</option>
                <option value="10">10</option>
                <option value="20">20</option>
                <option value="50">50</option>
                <option value="100">100</option>
            </select>
            <span class="showing-records">Showing <span v-if="filteredPersons.length < noOfRecords">{{ filteredPersons.length }}</span><span v-if="filteredPersons.length > noOfRecords">{{ noOfRecords }}</span> records.</span>
            <table id="data-table" v-if="personsLoaded">
                <tr>
                    <th v-for="(heading, x) in tableHeadings" :key="x">
                        {{ heading }}
                    </th>
                </tr>
                <tr v-for="(person, x) in filteredPersons" :key="x">
                    <td :class="getColorForName(person.accuracy.name_match.cosine_percentage, person.accuracy.dob_match.dob_flg, person.accuracy.dob_match.year_flg)">{{ person.docs[0].name }}</td>
                    <td>
                        <span v-for="(doc, y) in person.docs" :key="y">
                        {{ doc.doc_type}}
                        </span>
                    </td>
                    <td>
                        <span v-for="(doc, y) in person.docs" :key="y">
                        {{ doc.dob}}
                        </span>
                    </td>
                    <td :class="person.accuracy.name_match.cosine_percentage | getColor(person.accuracy.name_match.cosine_percentage)">
                        {{ person.accuracy.name_match.cosine_percentage}}
                    </td>
                    <td class="remarks">
                        <ul>
                            <li v-if="person.accuracy.name_match.cosine_percentage == 100 && person.accuracy.name_match.reorder_flg === false">Exact match</li>
                            <li v-if="person.accuracy.name_match.cosine_percentage == 100 && person.accuracy.name_match.reorder_flg === true">Exact match after re-ordering</li>
                            <li v-if="person.accuracy.name_match.reorder_flg === true">Name matched after re-ordering.</li>
                            <li v-if="person.accuracy.name_match.cosine_percentage <= 50">Fraud Detection</li>
                        </ul>
                    </td>
                    <td :class="( person.accuracy.dob_match.dob_flg || person.accuracy.dob_match.year_flg) | getColor(( person.accuracy.dob_match.dob_flg || person.accuracy.dob_match.year_flg))">
                        {{ person.accuracy.dob_match.dob_flg || person.accuracy.dob_match.year_flg }}
                    </td>
                    <td class="remarks">
                        <ul>
                            <li v-if="person.accuracy.dob_match.dob_flg === true">Exact match</li>
                            <li v-if="person.accuracy.dob_match.year_flg === true">Date matched by year</li>
                            <li v-if="person.accuracy.dob_match.dob_flg === false &&  person.accuracy.dob_match.year_flg === false">Fraud Detection</li>
                        </ul>
                    </td>
                </tr>
            </table>
            <div id="error" v-if="err">
                <h2>Oops. Please reload/check back after sometime.</h2>
            </div>
        </div>
        <div id="no-data" class="align-center" v-if="personsLoaded && persons.length === 0">
            No data. Please try again.
        </div>   
    </div>

</template>
<script>
import Statistics from './Statistics.vue';
export default {
   data() { 
    return {
      tableHeadings: ['Name', 'Document Type', 'DOB', 'Name Match', 'Remarks', 'DOB Match', 'Remarks'],
      persons: null,
      searchString: '',
      noOfRecords: 5,
      selectedPageNumber: 1,
      statsCreated: false,
      stats: {
          totalCount : 0,
          allMatches : 0,
          nameMismatch: 0,
          dobMismatch: 0,
          completeMismatch: 0,
          allMatchP : 0,
          nameMismatchP : 0,
          dobMismatchP : 0,
          completeMismatchP : 0
      },
      personsLoaded: false,
      err: false
    }
  },
  created() {
      this.fetchPerson();
  },    
  mounted() {
  },
  filters: {
      getColor(percentage) {
          if(percentage == undefined || null) {
              return 'red'
          } else if(percentage >= 70 || percentage === true) {
              return 'green'
          } else if(percentage >= 50) {
              return 'yellow'
          } else {
              return 'red'
          }
      },
  },
  computed: {
      filteredPersons(){
          if(this.searchString){
              return this.persons.filter((item)=>{
                  return item.docs[0].name.toLowerCase().includes(this.searchString.toLowerCase());
              }).slice(0, this.noOfRecords);
          } else{
              return this.persons.slice(0, this.noOfRecords);
          }
      },
  },  
  methods: {
      async createStats() {
        this.stats.totalCount = this.persons.length;
        await this.persons.forEach(ele => {
            if(ele.accuracy.name_match.cosine_percentage == 100 && (ele.accuracy.dob_match.dob_flg || ele.accuracy.dob_match.year_flg)) { this.stats.allMatches = this.stats.allMatches + 1;}
            else if(ele.accuracy.name_match.cosine_percentage != 100 && (ele.accuracy.dob_match.dob_flg || ele.accuracy.dob_match.year_flg)) { this.stats.nameMismatch = this.stats.nameMismatch + 1;}
            else if(ele.accuracy.name_match.cosine_percentage == 100 && (ele.accuracy.dob_match.dob_flg !== true || ele.accuracy.dob_match.year_flg!== true)) {this.stats.dobMismatch = this.stats.dobMismatch + 1}
            else { this.stats.completeMismatch = this.stats.completeMismatch + 1}
        });
        let allMatchP = (Math.round((this.stats.allMatches / this.persons.length * 100) * 10 ) / 10);
        let nameMismatchP = (Math.round(this.stats.nameMismatch / this.persons.length * 100) * 10) / 10;
        let dobMismatchP = (Math.round(this.stats.dobMismatch / this.persons.length * 100) * 10) / 10;
        let completeMismatchP = (Math.round(this.stats.completeMismatch / this.persons.length * 100) * 10) / 10;
        this.statsCreated = true;
        this.stats.allMatchP = allMatchP;
        this.stats.nameMismatchP = nameMismatchP;
        this.stats.dobMismatchP = dobMismatchP;
        this.stats.completeMismatchP = completeMismatchP;
      },
      async fetchPerson() {
          const response = await fetch('http://192.168.12.10:8080/verification/cdl/?format=json');
           const myJson = await response.json();
           this.persons = myJson;
           this.err = false;
           this.personsLoaded = true;
            this.createStats();
      },
      getColorForName(percentage, cond1, cond2) {
          if(percentage == undefined || null) {
              return 'red'
          } else if(percentage >= 70 && (cond1 || cond2 === true)) {
              return 'green'
          } else if(percentage >= 50 && (cond1 || cond2 === true) ) {
              return 'yellow'
          } else {
              return 'red'
          }
      },
  },
  components: {
      Statistics
  }
}

</script>
<style scoped>
.showing-records {
    font-size: 12px;
    font-weight: 500;
    opacity: 0.6;
}

.remarks {
    font-size: 12px;
}
</style>