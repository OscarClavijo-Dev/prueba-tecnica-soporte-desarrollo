<?php
/**
 * Plugin Name: GitHub Users Integration
 * Description: Consulta usuarios almacenados mediante la API REST de FastAPI.
 * Version: 1.0.0
 * Author: Oscar Clavijo
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Carga los estilos del plugin.
 */
function github_users_enqueue_styles() {
    wp_enqueue_style(
        'github-users',
        plugin_dir_url(__FILE__) . 'assets/css/github-users.css',
        array(),
        '1.0.0'
    );
}

add_action('wp_enqueue_scripts', 'github_users_enqueue_styles');

/**
 * Renderiza los usuarios obtenidos desde la API.
 *
 * @return string HTML generado para el shortcode.
 */
function github_users_shortcode() {
    $api_url = 'http://host.docker.internal:8000/api/users';

    $response = wp_remote_get(
        $api_url,
        array(
            'timeout' => 10,
            'headers' => array(
                'Accept' => 'application/json',
            ),
        )
    );

    if (is_wp_error($response)) {
        return '<div class="github-users-message github-users-message--error">
            No fue posible consultar la API de usuarios.
        </div>';
    }

    $status_code = wp_remote_retrieve_response_code($response);

    if ($status_code !== 200) {
        return '<div class="github-users-message github-users-message--error">
            La API respondió con un error HTTP (' . esc_html($status_code) . ').
        </div>';
    }

    $body = wp_remote_retrieve_body($response);
    $users = json_decode($body, true);

    if (!is_array($users)) {
        return '<div class="github-users-message github-users-message--error">
            La respuesta de la API no tiene un formato válido.
        </div>';
    }

    if (empty($users)) {
        return '<div class="github-users-message github-users-message--empty">
            No hay usuarios almacenados.
        </div>';
    }

    $html = '<section class="github-users" aria-labelledby="github-users-title">';
    $html .= '<div class="github-users__header">';
    $html .= '<h2 id="github-users-title">Usuarios de GitHub</h2>';
    $html .= '<p>Usuarios almacenados en la API REST propia.</p>';

    $html .= '<div class="github-users__api-info">';
    $html .= '<p><strong>API REST:</strong> GET /api/users</p>';
    $html .= '<a class="github-users__api-link" href="http://127.0.0.1:8000/api/users" target="_blank" rel="noopener noreferrer">';
    $html .= 'Consultar API REST';
    $html .= '</a>';
    $html .= '</div>';

    $html .= '</div>';

    foreach ($users as $user) {
        $login = isset($user['login']) && $user['login']
            ? $user['login']
            : 'Sin login';

        $name = isset($user['name']) && $user['name']
            ? $user['name']
            : 'Sin nombre';

        $email = isset($user['email']) && $user['email']
            ? $user['email']
            : 'Sin email';

        $avatar_url = isset($user['avatar_url']) && $user['avatar_url']
            ? $user['avatar_url']
            : '';

        $html_url = isset($user['html_url']) && $user['html_url']
            ? $user['html_url']
            : '';

        $html .= '<article class="github-user-card">';

        if ($avatar_url) {
            $html .= '<img class="github-user-card__avatar" src="' . esc_url($avatar_url) . '" alt="Avatar de ' . esc_attr($login) . '" loading="lazy">';
        } else {
            $html .= '<div class="github-user-card__avatar github-user-card__avatar--placeholder" aria-hidden="true">';
            $html .= esc_html(strtoupper(substr($login, 0, 1)));
            $html .= '</div>';
        }

        $html .= '<div class="github-user-card__content">';

        $html .= '<h3 class="github-user-card__login">';
        $html .= esc_html($login);
        $html .= '</h3>';

        $html .= '<p class="github-user-card__name">';
        $html .= esc_html($name);
        $html .= '</p>';

        $html .= '<p class="github-user-card__email">';
        $html .= esc_html($email);
        $html .= '</p>';

        if ($html_url) {
            $html .= '<a class="github-user-card__link" href="' . esc_url($html_url) . '" target="_blank" rel="noopener noreferrer">';
            $html .= 'Ver perfil en GitHub';
            $html .= '</a>';
        }

        $html .= '</div>';
        $html .= '</article>';
    }

    $html .= '</div>';
    $html .= '</section>';

    return $html;
}

add_shortcode('github_users', 'github_users_shortcode');
