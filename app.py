import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
from flask_pymongo import PyMongo
from bson.binary import Binary
import gridfs
import base64
from datetime import datetime,date,timedelta
import dash_ui as dui
import io
from flask import render_template

from server import server
app = dash.Dash(
    __name__,
    auth='auth',
    server=server,
    url_base_pathname="/",
    external_stylesheets=["https://codepen.io/rmarren1/pen/mLqGRg.css","https://codepen.io/chriddyp/pen/bWLwgP.css"],
)
app.title = 'vllgrs'

uri = "mongodb://localhost:27017"
mongo = PyMongo(
    server,
    uri
)
db = mongo.cx.vllgrs

@server.route("/")
def MyDashApp():
    return app.index()

grid = dui.Grid(
    _id='grid',
    num_rows=12,
    num_cols=12,
    grid_padding=0,
)

grid.add_element( # top bar
    col=1,row=1,width=12,height=1,
    element= html.Div(
        id='top-div',
        style=dict(backgroundColor="skyBlue",height="95%",width="100%",textAlign='center'),
        children=[
            html.Div( # top right - site name
                id = "top-div-left",
                style=dict(display="inline-block",width="25%",padding="0px",paddingBottom="0px",paddingTop="0px",fontSize="40px",),
                children = dcc.Markdown(
                    id="brand-text",
                    children="VLLGRS",
                )
            ),
            html.Div( # empty
                id='top-div-middle',
                style=dict(display='inline-block',width='50%',opacity='0%')
            ),
            html.Div( # empty
                id = "top-div-right",
                style=dict(display="inline-block",width="25%"),
                children = ""
            ),
        ] # end children
    )
)
grid.add_element( # left side content/info div
    col=1,row=2,width=3,height=6,
    element=html.Div(
        children=[
            html.H3("This is the div that shows content/info related to what you've clicked on!")
        ],
        id='upper-left-div',
        style=dict(backgroundColor='#ABEBC6',height="95%",width="95%",textAlign='center',margin='auto',paddingTop="10px"),
    )
)
grid.add_element( # post div
    col=4,row=1,width=6,height=2,
    element=html.Div(
        id = 'middle-upper-div',
        style=dict(backgroundColor='#ECF0F1',height="100%",width="100%",margin='auto',textAlign='left',),
        children = [
            html.Div( # post div
                id = 'post-div',
                style=dict(height="68%",borderBottom='2px solid darkGreen',),
                children = [
                    dcc.RadioItems(
                        id='post-type-radio',
                        options = [dict(label="TEXTLET",value="textlet"),dict(label="TEXT",value="text")],
                        value="textlet",
                        style=dict(display="inline-block",width="15%",verticalAlign='top',fontSize='20px')
                    ),
                    dcc.Textarea(
                        id='post-input',
                        style=dict(display="inline-block",width="50%",height="95%",margin='auto',fontSize='20px',whiteSpace='normal')
                    ),
                    dcc.RadioItems(
                        id='post-privacy-radios',
                        options = [dict(label="HUT 🏠",value="hut"),dict(label="VLLG 🌆",value="vllg"),dict(label="VLLY 🌎",value="vlly")],
                        value='vllg',
                        style=dict(display="inline-block",width="15%",verticalAlign='top',fontSize='15px')
                    ),
                    html.Button(
                        id='post-submit-button',
                        children="SUBMIT POST",
                        style=dict(display='inline-block',height="50%",verticalAlign="top",width="15%",fontSize="15px",backgroundColor="white",border="2px solid darkGreen",whiteSpace='normal',lineHeight='normal'),
                    ),
                ]
            ),
            html.Div( # context selector - hut, vllg, vlly
                id='context-selector',
                style=dict(width="60%",height="28%",textAlign='center',margin='auto',paddingTop="5px"),
                children = [
                    html.Button(
                        id='hut-button',
                        children="HUT",
                        style=dict(display="inline-block",backgroundColor="white",height="100%",width="29%",padding="1%",border="2px solid darkGreen",fontSize="20px")
                    ),
                    html.Button(
                        id='vllg-button',
                        children="VLLG",
                        style=dict(display="inline-block",backgroundColor="white",height="100%",width="29%",padding="1%",border="2px solid darkGreen",fontSize="20px")
                    ),
                    html.Button(
                        id='vlly-button',
                        children="VLLY",
                        style=dict(display="inline-block",backgroundColor="white",height="100%",width="29%",padding="1%",border="2px solid darkGreen",fontSize="20px")
                    ),
                ]
            )      
        ]
    )
)
grid.add_element( # vllg feed & blog writing divs
    col=4,row=3,width=6,height=9,
    element=html.Div(      
        id='middle-lower-div',
        style=dict(backgroundColor='white',height="95%",width="100%",margin='auto',textAlign='center',),
        children=[
            dcc.Tabs(
                id='feed-blog-tabs',
                style=dict(height="40px",padding="0px",fontSize="15px",fontWeight="bold",verticalAlign='top'),
                children = [
                    dcc.Tab( # social feed
                        id="social-feed-tab",
                        label='FEED',
                        selected_style=dict(backgroundColor='forestGreen',color='white'),
                        children = html.Div([
                            html.H3("This is the div where the content gets shown")
                        ])
                    ),
                    dcc.Tab( # blog writing
                        id='blog-writing-tab',
                        label='WRITE A BLOG POST',
                        selected_style=dict(backgroundColor='forestGreen',color='white'),
                        children = dcc.Tabs(
                            id='blog-writing-tab-tabs',
                            style=dict(height="40px",fontWeight='bold'),
                            children = [
                                dcc.Tab( # writing
                                    id='blog-writing-markdown',
                                    label='WRITE',
                                    selected_style=dict(backgroundColor='lightBlue'),
                                    children=[
                                        dcc.Textarea(
                                            id='blog-writing-markdown-textarea',
                                            style=dict(height="30vw",width="45vw",fontSize="18px"),
                                            placeholder = "What are you thinking about?"
                                        )
                                    ]
                                ),
                                dcc.Tab( # previewing
                                    id='blog-writing-markdown-preview',
                                    label='PREVIEW MARKDOWN',
                                    selected_style=dict(backgroundColor='lightBlue',),
                                    children = [
                                        dcc.Markdown(
                                            id='markdown-preview-renderer',
                                            containerProps=dict(
                                                style=dict(textAlign='left', margin='20px',maxWidth='600px',fontSoze="40px")
                                            )
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        ],
    )
)
grid.add_element( # bottom left config div
    col=1,row=8,width=3,height=5,
    element=html.Div(
        id="bottom-left-div",
        style=dict(height="95%",width="92%",textAlign='center',margin='auto'),
        children="",
    ),
)
grid.add_element( # bottom right config div
    col=10,row=8,width=3,height=5,
    element=html.Div(
        id="bottom-right-div",
        style=dict(height="95%",width="95%",textAlign='center',margin='auto'),
        children=[
            html.Div(
                id='user-settings-div',
                style=dict(display="none",height="100%",width="100%",backgroundColor="#ABEBC6",textAlign='center',overflow='auto'),
                children=[
                    html.Div([
                        html.H4("Setting 1"),
                        dcc.Dropdown(
                            id='fake-setting-dropdown-1',
                            options=[dict(label="Option 1",value=1),dict(label="Option 2",value=2)],
                            style=dict(display='block',height="40%",width="100%"),
                        ),
                    ]),
                    html.Div([
                        html.H4("Setting 2"),
                        dcc.Dropdown(
                            id='fake-setting-dropdown-2',
                            options=[dict(label="Option 1",value=1),dict(label="Option 2",value=2)],
                            style=dict(display='block',height="40%",width="100%"),
                        )
                    ]),
                    html.Button(
                        id='submit-user-settings-button',
                        n_clicks=0,
                        style=dict(display='block',height="12%",width="100%",fontSize="15px",backgroundColor="white",border="2px solid darkGreen",lineheight="normal",whiteSpace='normal'),
                        children="Submit Changes ✅ or Close"
                    )
                ]
            )
        ],
    ),
)
def return_user_profile_div(): # future parameters: user, cache (T/F), size, shape, etc.
    img_path = 'hat.jpg' # pull the picture object from the database based on the user (no need to cache - it stays the entire time the user is logged in? Maybe cache it for the session)
    return base64.b64encode(open(img_path,'rb').read()) # encode the picture
grid.add_element( # in profile column
    col=10,row=2,width=3,height=6,
    element=html.Div(
        id = "upper-right-div",
        style=dict(backgroundColor='#ABEBC6',height="95%",width="92%",textAlign='center',margin='auto'),
        children = [ 
            html.Div([ 
                html.Button(
                    id = "user-profile-pic-button",
                    style=dict(width="40%",height="50%",whiteSpace='normal',lineHeight='normal',padding="0px"),
                    children=[
                        html.Img(
                            src='data:image/jpg;base64,{}'.format( return_user_profile_div().decode() ),
                            style=dict(width="100%",height="10%",overflow="hidden"),
                        ),
                    ],
                ),
                html.Div([
                    html.H3("Russell Romney",style=dict(paddingTop="0px")), # pull user's name based off of session _id
                    html.Button(id='user-profile-bio',children="Python dev. Books.",style=dict(border="0px",fontSize="15px",textAlign='center')) # user will be able to change this emoji
                ]),
                html.Button( # clicking this does some undetermined thing
                    id="user-settings-button",
                    children="Settings 🔧",
                    n_clicks=0,
                    style=dict(fontSize="20px",backgroundColor='white',border="2px solid darkGreen")
                ),
            ])
        ],
    )
)




app.layout = html.Div(
    dui.Layout(
        grid=grid
    ),
    style=dict(width="100vmax",height="100vmin",margin='auto',overflow='auto')
)





# show settings div on settings click
@app.callback(
    Output("user-settings-div","style"),
    [Input('user-settings-button','n_clicks'),
     Input("submit-user-settings-button","n_clicks")])
def show_user_settings(n_clicks_settings,n_clicks_submit):
    if n_clicks_settings==0 and n_clicks_submit==0:
        return dict(display="none",height="100%",width="100%",backgroundColor="#ABEBC6",textAlign='center',overflow='auto')
    elif n_clicks_settings-n_clicks_submit==0:
        return dict(display="none",height="100%",width="100%",backgroundColor="#ABEBC6",textAlign='center',overflow='auto')
    return dict(height="100%",width="100%",backgroundColor="#ABEBC6",textAlign='center')

@app.callback(
    Output("markdown-preview-renderer",'children'),
    [Input("blog-writing-markdown-textarea",'value')])
def make_markdown_previewed_again(text_):
    if not text_:
        return ""
    print(text_)
    return text_

# counts the number of words/characters in your text/textlet post, turn red if the number goes over depending on the post_type
# counts the number of words in your blog post, estimates reading time, turns red if the number goes over 5,000
# warn you from leaving if you have unsaved content in the blog post section
# submits settings changes
# posts a post
# posts a comment
# generates feed content & store in Store
    # depends on vllg context - but either way, it stores it in the browser
    # maybe create preexisting hidden buttons for commenting and upvoting - 20 preexisting buttons (for 20 pieces of content per page)
        # each time the user moves to the next page, the buttons get reassigned to the next 1-20 content pieces
        # ...how to deal with a potentially unlimited amount of comments?
    # generate next page of feed content & store in Store as next page i.e. dict(page1:[content1,content2...],page2:[content1,content2...]...)


if __name__=="__main__":
    server.run(
        debug=False,
        threaded=True
    )