program Fibonacci;

var
   Fibonacci1 : integer;
   Fibonacci2 : integer;
   temp : integer;
   count : integer;

begin
   write('First ten Fibonacci numbers are: \n');
   count := 0;
   Fibonacci1 := 0;
   Fibonacci2 := 1;
   repeat
      write(Fibonacci2 div 7);
      temp := Fibonacci2;
      Fibonacci2 := Fibonacci1 + Fibonacci2;
      Fibonacci1 := Temp;
      count := count + 1;
   until count = 10;
   write('\n');

end.