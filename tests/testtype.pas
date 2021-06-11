program testtype;
var
    A : real;
    B : boolean;
    C : boolean;
function Summation(num : integer; real1 : real; bool1 : boolean; str : string) : string;
begin
    if num = 1 then
    begin
        Summation := 'Hello';
    end
    else
    begin
        Summation := 'World';
    end;
end;

begin
    A := 22.5;
    A := a + Summation( 10, 2.0, true, 'Hello');
    B := true;
    C := false;
end.