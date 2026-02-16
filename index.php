<?php
/**
 *Plugin Name: Library
 * Version: 1.0
 */



add_action('init', 'library_init');
function library_init(){
    register_post_type('books', [
        'public' => true,
        'label' => [
            'name' => 'Books',
            'singular_name' => 'Book',
        ],
        'has_archive' => true,
        'supports' => ['title', 'editor', 'thumbnail']
        'show_in_rest' => true,
        'menu_position' => 5, //guternberg support
    ]);
}

add_shortcode('latest_books', 'library_latest_books');
function library_latest_books(){
    $args = [
        'post_type' => 'books',
        'limit' => 5
        'order' => 'desc',
        'orderby' => 'date',
    ];
    
    $query = new WP_Query($args);

    if(!$query->have_posts){
        return 'No post found';
    }
    ob_start();

    while($query->have_post){
        $query->the_post;
        ?>
        <div:book-item>
            <h1><?php esc_html(get_the_title())?></h1>
            <p><?php esc_html(get_the_excerpt())?></p>
        </div>
        <?php
    }

    wp_reset_post_data();
    return ob_get_clean();
    

}

add_action('save_post', 'books_save_author_meta');

function books_save_author_meta($post_id) {

    // 1. Check nonce
    if (
        !isset($_POST['books_author_nonce_field']) ||
        !wp_verify_nonce($_POST['books_author_nonce_field'], 'books_author_nonce')
    ) {
        return;
    }

    // 2. Prevent autosave
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // 3. Permission check
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    // 4. Sanitize and save
    if (isset($_POST['books_author'])) {
        update_post_meta(
            $post_id,
            '_books_author',
            sanitize_text_field($_POST['books_author'])
        );
    }
}


register_activation_hook(__FILE__, 'create_table_schema_on_activation');
function create_table_schema_on_activation(){
    global $wpdb;
    $table_name = $wbdb->prefix . 'books';
    $charset = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id midiumint(9) NOT NULL AUTO_INCREMENT,
        title varchar(255) NOT NULL,
        author varchar(255) NOT NULL,
        editor varchar(255) NOT NULL,
        content varchar(255) NOT NULL,
        thumbnail varchar(255) NOT NULL,
        PRIMARY KEY (id)
    ) $charset";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql);
}
$wpdb->insert();
$wpdb->get_results();
add_action('rest_api_init', 'rest_api_init');
function rest_api_init(){
    register_rest_route('library/v1', '/books', [
        'method' => 'GET',
        'callback' => 'library_get_books',
        'permission_callback' => function(){
            return current_user_can('edit_post');
        }
    ]);
        }
    ]);
}

?>