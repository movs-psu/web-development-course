<template>
  <li :style="'color: ' + todo.color">
    <s v-if="todo.done">{{ todo.title }}</s>
    <span v-else>{{ todo.title }}</span>
    <button type="button" @click="$emit('toggle', !todo.done)">Toggle</button>
  </li>
</template>

<script>
export default {
  props: { todo: { type: Object, required: true } },
};
</script>

<style scoped></style>
