
{
   "_id": ObjectId("5222f8e0d85242c01100000d"),
   "name": "Richard Garry",
   "profile_pic": "profile_pic_3.jpg" 
}



{
   "_id": ObjectId("5222f885d85242c011000009"),
   "post_author_id": ObjectId("5146bb52d8524270060001f4"),
   "post_text": "Let's get started !!!\t\t\t",
   "timestamp": "Sun, 01-Sep-2013",
   "total_comments": NumberInt(3),
   "total_likes": NumberInt(2) ,
   "likes_user_ids": {
     "0": ObjectId("52147f70d85242cc12000010"),
     "1": ObjectId("5222f8e0d85242c01100000d") 
  },
   "comments": {
     "0": {
       "comment_id": ObjectId("5222f897d85242c01100000a"),
       "comment_user_id": ObjectId("52147f70d85242cc12000010"),
       "comment_text": "This is comment 1 !!" 
    },
     "1": {
       "comment_id": ObjectId("5222f8a7d85242c01100000b"),
       "comment_user_id": ObjectId("5222f8e0d85242c01100000d"),
       "comment_text": "This is comment 2 !!" 
    } 
  }
}

<div id="div_post_content">
    <textarea id="post_textarea">
    </textarea>
</div>
<div class="div_post_submit">
    <input type="button" value="Create New Post" id="btn_new_post" class="button_style"/>
</div>

foreach($posts_cursor as $post)
{
    $post_id=$post['_id'];
    $post_text=$post['post_text'];
    $post_author_id=$post['post_author_id'];

$collection = $database->selectCollection('users');
$post_author_details = $collection->findOne(array('_id' =>$post_author_id));
$post_author = $post_author_details['name'];
$post_author_profile_pic = $post_author_details['profile_pic'];



$post_like_unlike_id=$post_id.'_like_unlike';
$post_like_count_id=$post_id.'_like_count';
$post_comment_count_id = $post_id.'_comment_count';
$post_self_comment_id=$post_id.'_self_comment';
$post_comment_text_box_id=$post_id.'_comment_text_box';

if(in_array($_SESSION['user_id'],$post['likes_user_ids']))
{
   $like_or_unlike='Unlike';
}
else
{
 $like_or_unlike='Like';
}

// you can also write this in short ternary form:

$like_or_unlike = (in_array($_SESSION['user_id'],$post['likes_user_ids'])) ? 'Unlike' : 'Like';

<div class="comments_wrap">
    <span>
        <span><img src="images/like.png" /></span>     
        <span class="post_feedback_like_unlike" id="<?php echo $post_like_unlike_id;?>"><?php echo $like_or_unlike; ?></span>                    
        <span class="post_feedback_count" id="<?php echo $post_like_count_id; ?>"><?php echo $post_like_count;?></span>
    </span>
    <span>
        <span class="post_feedback_comment"> <img src="images/comment.png" /> Comment</span>               <span class="post_feedback_count" id="<?php echo $post_comment_count_id; ?>"><?php echo                     $post_comment_count;?></span>
    </span>
</div>


<div class="post_wrap" id="<?php echo $post['_id'];?>">
<div class="post_wrap_author_profile_picture">
    <img src="images/<?php echo $post_author_profile_pic;?>" />
</div>  
<div class="post_details">  
          <div class="post_author">
        <?php echo $post_author ?> 
    </div>
    <div class="post_text">
        <?php echo $post_text; ?>
    </div>
</div>

