# 0406_homework

1. (a) : {% url 'reservations:update' reservation.pk %}

   (b) : {% csrf_token %}

   (c) : value='{% reservation.name %}'

   (d) : value='{% reservation.date %}'

   

2. (a) : reservations:delete

   

3. (a) : reservation_id

   (b) : delete

   (c) : reservations:index

   

4. GET : url로 내용들을 보내고 받는 것

   POST : db의 내용들을 보내고 받는 것

