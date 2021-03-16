<template>
  <div>
    <h2>Canais</h2>
    <ul>
      <li
        class="btn btn-success"
        @click="loadChan(canal.id)"
        v-for="canal in canais"
        :key="canal.id"
      >
        {{ canal.titulo }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    name: 'MeusCanais',
    props: ['canais'],
    methods: {
        loadChan: function (id) {
            let texto;
            for (let y of this.canais) {
                if (y.id == id) {
                    texto = y.titulo;
                }
            }
            console.log(`Faz de conta que abri o canal ${texto}`)
            this.$emit('mudacanal', id);
        }
    }
};
</script>

<style>
</style>