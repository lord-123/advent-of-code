-module(aoc1).
-export([solve/0]).

add_lists(A,B, {L,R}) ->
    {L ++ [A], R ++ [B]}.

parse_input(IoDevice) ->
    case io:fread(IoDevice, "", "~d   ~d") of
        {ok, [A, B]} -> add_lists(A, B, parse_input(IoDevice));
        eof -> {[], []}
    end.

get_input() ->
    {ok, IoDevice} = file:open("1.in", [read]),
    {L, R} = parse_input(IoDevice),
    {lists:sort(L), lists:sort(R)}.

p1({[], []}) -> 0;
p1({[Li | L], [Ri | R]}) ->
    abs(Li-Ri) + p1({L, R}).

count([]) ->
    #{};
count(L) -> count(L, #{}).
count([Head | Tail], M) ->
    N = case maps:is_key(Head, M) of
        true -> #{Head := X} = M,
                X + 1;
        false -> 1
    end,
    count(Tail, M#{Head => N});
count([], M) -> M.



p2({L, R}) ->
    Cl = count(L),
    Cr = count(R),
    F = fun(Key, Val, Acc) ->
        Key * Val * maps:get(Key, Cr, 0) + Acc end,
    maps:fold(F, 0, Cl).

solve() ->
    Input = get_input(),
    io:fwrite("p1: ~w~n", [p1(Input)]),
    io:fwrite("p2: ~w~n", [p2(Input)]).