module Main exposing (..)

import Browser
import Html exposing (Html, text, div, h1, h5, img, input, button, Attribute , table, thead, tbody, tr, td, th, p, span)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput, onClick)
import Http
import Json.Decode exposing (Decoder, field, string, int, map2, map3, map)
import String exposing(isEmpty)
import String.Extra exposing(toTitleCase)
apiUrl : String
apiUrl = "http://localhost:5000/json"

comboUrl : String
comboUrl = "http://localhost:5000/stat"

---- MODEL ----


type alias Model =
    {
        name: String
        , adjective: String
        , timestamp: String
    }

-- type alias Config = 
-- {
--     url : String
-- }


composeText : Model -> String
composeText model =
    model.name ++ " " ++ model.adjective

fetchData : Cmd Msg
fetchData = 
    Http.get 
    { url = apiUrl
     , expect  = Http.expectJson Update jsonDecoder
    }

        
     
jsonDecoder : Decoder Model
jsonDecoder = 
   map3 Model 
    (field "adjective" string)
    (field "name" string)
    (field "timestamp" string)

init : ( Model, Cmd Msg )
init =
    ( Model "" "" "", Cmd.none )



---- UPDATE ----


type Msg
    = NoOp
    | Update (Result Http.Error Model)
    | LoadData
    | Reset


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NoOp ->
            ( model, Cmd.none )
        LoadData ->
            ({ model | name = "Fetching", adjective = "Fetching..." }, fetchData)
        Update result ->
            case result of
                Ok data ->
                    ({model | name = data.name, adjective = data.adjective, timestamp = data.timestamp}, Cmd.none)
                Err errorMsssage ->
                    ({model | name ="Failed!", adjective="Br0ken!"}, Cmd.none)
        Reset ->
            ( { model | name = "", adjective = ""}, Cmd.none)



---- VIEW ----


view : Model -> Html Msg
view model =
    div  [classList[("container", True)]][
    div [class "d-flex justify-content-center"][
        h1 [ class "header" ][text "Name Generator"]
    ]
    , div [ class "jumbotron"][
        div [class "d-flex justify-content-center"][
            p [ class "maintext"][
            text ( 
                if (isEmpty model.name) || (isEmpty model.adjective) then
                    "-"
                else 
                    String.Extra.toTitleCase (model.name ++ " " ++ model.adjective)
                    )

            ]

        ]
        , div [class "d-flex justify-content-center" ][
            h5 [][text "Id"]
        ]
        , div [class "d-flex justify-content-center"][
            span [ classList[("badge", True), ("badge-dark", True)]][ 
            text ( 
                if (isEmpty model.name) || (isEmpty model.adjective) then
                    "-"
                else 
                    String.replace " " "-" model.name ++ "-" ++ String.replace " " "-" model.adjective
                    )

            ]
        ]
    ]

    ,div [ classList[("d-flex justify-content-center", True)] ][
        div [class "btn-toolbar"][
            div [ class "btn-group"][
                button [ onClick (LoadData) , type_ "button", classList[("btn", True), ("btn-primary", True), ("btn-lg", True)]] [text "Generate!"]
            ]
            , div [ class "btn-group"][
                button [ onClick (Reset ), type_ "button", classList[("btn", True), ("btn-danger", True),  ("btn-lg", True)] ] [text "Reset"]
            ]
        ]
   
    ]
    , div [class "d-flex justify-content-center"][
            p [ class "subtext" ][
            text ( 
                if (isEmpty model.timestamp)  then
                    ""
                else 
                    "Generated at " ++ model.timestamp
                    )
            ]
    ]
    , div [class "d-flex justify-content-center"][
        p [class "subtext" ][ text "Generating names out of 165 784 possible cominations"]
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
