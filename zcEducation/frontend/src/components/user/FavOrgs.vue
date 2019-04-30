<template>
  <div class="messagelist">
    {% for org in org_list %}
    <div class="messages butler_list company company-fav-box">
      <dl class="des fr">
        <dt>
          <a href="{% url 'orgs:org_detail' org.id %}">
            <img width="160" height="90" src="{{ MEDIA_URL }}{{ org.image }}">
          </a>
        </dt>
        <dd>
          <h1>
            <a href="{% url 'orgs:org_detail' org.id %}">{{ org.name }}</a>
          </h1>
          <div class="pic fl" style="width:auto;"></div>
          <span class="c8 clear">{{ org.address }}</span>
          <div class="delete jsDeleteFav_org" data-favid="{{ org.id }}"></div>
        </dd>
      </dl>
    </div>
    {% endfor %}
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
</style>
