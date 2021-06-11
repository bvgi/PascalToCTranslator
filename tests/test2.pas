program test2;
        var
            A : integer;

            procedure ScopeInner;
            var A : integer;
            begin
                A := 10;
                writeln(A);
                if num = 1 then
                begin
                    Summation := 1;
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
            writeln(A + 1 * 2);
            ScopeInner;
            A := a + Summation( 10 );
            writeln(a);
            writeln(A);
        end.