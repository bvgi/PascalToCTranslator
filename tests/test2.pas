program test2;
var
    A : integer;

procedure ScopeInner;
var ten : integer;
begin
    ten := 10;
    write(ten);
    if ten = 10 then
    begin
        ten := 1;
    end;
end;

function Summation(num : integer) : integer;
begin
    if num = 1 then
    begin
        Summation := 1;
    end
    else
    begin
        Summation := 2;
    end;
end;

begin
    A := 20;
    write(A + 1 * 2);
    ScopeInner;
    A := a + Summation( 10 );
    write(a);
end.