# 0407_Homework

1. 모델폼 정의를 위한 코드

   (a) : forms.ModelForm

   (b) : Meta

2. 글 작성 코드 문제 발생 이유와 해결방안

   ```python
   def create(request):
       if request.method == 'POST':
           form = ReservationForm(request.POST)
           if form.is_valid():
               article = form.save()
               return redirect('reservations:detail', reservation.id)
       else:
           form = ReservationForm()
           '''
           context = {
               'form': form,
           }
           return render(request, 'reservations/create.html', context)
           '''
       context = {
           'form': form,
       }
       return render(request, 'reservations/create.html', context)
   ```

   이유 :  주석 처리된 부분이 else의 안쪽에 들어있기 때문에 form이 POST 요청으로 왔지만 유효하지 않은 경우에 form값이 전달되지 않을 뿐더러 return 값이 존재하지 않는다.

   해결방안 : 위 코드처럼 indentation을 당겨서 if 문 바깥쪽에 작성한다.

3. 글 수정 기능 구현 코드

   (a) : form = ReservationForm(request.POST, instance=reservation)

   (b) : form = ReservationForm(instance=reservation)

4. 글 수정 기능 구현 코드 모두

   (a) : as_p, as_ul, as_table