<template>
    <slim-grid :data="data" :show-pager="false" :auto-height="true" :editable="true"></slim-grid>
</template>

<script>
import SlimGrid from 'vue-slimgrid';

export default {
  components: { SlimGrid },
  props: ['columnNames'],
  data() {
    return {
      data: this.initializeData(this.columnNames),
    };
  },
  methods: {
    initializeData(columnNames) {
      const row = { id: 0 };
      const data = [];
      for (let i = 0; i < columnNames.length; i += 1) {
        row[columnNames[i]] = '';
      }
      data.push(row);
      return data;
    },
  },
};
</script>

<style src="../../node_modules/vue-slimgrid/dist/slimgrid.css"></style>
