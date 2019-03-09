module Main exposing (..)

import Browser
import Html exposing (Html, text, div, h1, img, input, Attribute)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput)


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
   -- | GetData String String


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NoOp ->
            ( model, Cmd.none )
        Change newModel ->
            ({ model | name = newModel.name, adjective = newModel.adjective }, Cmd.none)
      --  GetData newName new            



---- VIEW ----


view : Model -> Html Msg
view model =
    div []
        [ img [ src "/logo.svg" ] []
        , h1 [] [ text (composeText model) ]
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
