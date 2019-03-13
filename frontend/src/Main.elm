module Main exposing (..)

import Browser
import Html exposing (Html, text, div, h1, img, input, button, Attribute , table, thead, tbody, tr, td, th)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput, onClick)


---- MODEL ----


type alias Model =
    {
        name: String
        , adjective: String
        , timestamp: String
    }


composeText : Model -> String
composeText model =
    model.name ++ " " ++ model.adjective

init : ( Model, Cmd Msg )
init =
    ( Model "Generated name" "Generated adjective" "", Cmd.none )



---- UPDATE ----


type Msg
    = NoOp
    | Change Model
    | Generate String String
    | Reset


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NoOp ->
            ( model, Cmd.none )
        Change newModel ->
            ({ model | name = newModel.name, adjective = newModel.adjective }, Cmd.none)
        Generate newName new  ->
            ( { model | name = newName, adjective = new}, Cmd.none)         
        Reset ->
            ( { model | name = "", adjective = ""}, Cmd.none)



---- VIEW ----


view : Model -> Html Msg
view model =
    div  [classList[("container", True)]][
        h1 [][text "Generator"]
    , div [class "row"][
        text ( model.name ++ " " ++ model.adjective)
    ]
    ,div [ class "row" ][
         button [ onClick (Generate "jada" "neida" ), type_ "button", classList[("btn", True), ("btn-primary", True)]] [text "Generate!"]
         , button [ onClick (Reset ), type_ "button", classList[("btn", True), ("btn-danger", True)] ] [text "Reset"]

        ]
    ]
    


---- PROGRAM ----


main : Program () Model Msg
main =
    Browser.element
        { view = view
        , init = \_ -> init
        , update = update
        , subscriptions = always Sub.none
        }
